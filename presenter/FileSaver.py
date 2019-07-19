from properties import DATA_FOLDER, FILE_STORAGE_EXTENSION


class FileSaver(object):
    name = ""
    __file = ""

    def __init__(self,name):
        self.name = name
        self.__file = DATA_FOLDER + name + FILE_STORAGE_EXTENSION

    def __open_file(self):
        None

    def add_presence(self,time, status):
        None

    def close_file_saver(self):
        None