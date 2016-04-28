class FileProcessor:

    def __init__(self, file_path):
        self.file_path = file_path

    def filtered_lines(self, filter_function):
        with open(self.file_path) as a_file:
            unfiltered_lines = a_file.readlines()
            return filter(filter_function, unfiltered_lines)
