import os, zipfile


class Repository:
    def __init__(self, root_path):
        self.root_path = root_path
        self.extension = '.htmlz'
        self.contents = os.listdir(self.root_path)

    def list_books(self) -> list:
        # the names of all books sans extension
        return [name[0: len(name) - len(self.extension)] for name in self.contents if name.endswith(self.extension)]

    def get_path(self, name: str) -> str:
        extracted_path = os.path.join(self.root_path, name)
        index_path = os.path.join(extracted_path, 'index.html')
        archive_path = extracted_path + self.extension

        file_name = name + self.extension
        if file_name not in self.contents:
            # The book isn't in the repository
            return None
        if name in self.contents:
            # The book is in the repository and the archive is extracted
            return index_path

        # The book is in the repository, but the archive is not extracted
        with zipfile.ZipFile(archive_path) as zf:
            zf.extractall(extracted_path)

        return index_path
