FROM python:3.5

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python", "gevent_srv.py"]



