import mimetypes, os, urllib
from repository import Repository
from flask import Flask, request, g, send_file, abort, \
     render_template, Response

# default configuration
DATABASE = os.getenv('HTMLZ_REPO', '/storage/Served EBooks')

# create app object
app = Flask(__name__)


def get_repo():
    # This attaches a repository instance to "g" or the global request context.
    # This way, only one database connection per http request gets created, even if you
    # make multiple calls to get_repo().
    repo = getattr(g, 'repository', None)
    if repo is None:
        repo = Repository(DATABASE)
        g.repository = repo

    return repo


# called automatically when we're done a request
@app.teardown_appcontext
def teardown(exception):
    if exception is not None:
        print(exception)


@app.route('/')
def list_books() -> object:
    books = get_repo().list_books()

    base_path = request.headers.get('X-Request-Uri')
    if base_path is None:
        base_path = ''

    return render_template('list_books.html', books=books, base_path=base_path)


@app.route('/<name>')
def view_book(name: str) -> object:
    if '.css' in name:
        referer = request.headers.get('Referer')
        resource_name = parse_referer(referer)
        path = os.path.join(get_repo().root_path, resource_name, name)
        return create_file_response(path)

    path = get_repo().get_path(name)

    if path is None:
        abort(404)  # 404 Not Found

    return create_file_response(path)


@app.route('/images/<name>')
def view_resource(name: str):
    referer = request.headers.get('Referer')
    resource_name = parse_referer(referer)
    path = os.path.join(get_repo().root_path, resource_name, 'images/', name)
    return create_file_response(path)


def parse_referer(value: str) -> str:
    sections = value.split('/')
    url_encoded_referer = sections[len(sections) - 1]
    return urllib.parse.unquote(url_encoded_referer)


def create_file_response(path: str) -> object:
    m_type = mimetypes.guess_type(path)[0]
    try:
        return send_file(path, mimetype=m_type)
    except IOError as e:
        return Response(e, mimetype='application/plain', status=400)


if __name__ == '__main__':
    # This code path should run for development only.
    # gevent_srv.py should be used in a production environment
    app.run(debug=True, threaded=True, host='0.0.0.0')
