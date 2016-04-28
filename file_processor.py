class FileProcessor:

    def __init__(self, file_path):
        self.file_path = file_path

    def lines(self):
        with open(self.file_path) as a_file:
            return a_file.readlines()
