from abc import ABCMeta, abstractmethod
import pickle
import shelve


class Director(object):
    def __init__(self, data_builder):
        self.data_builder = data_builder

    def construct_data(self):
        self.data_builder.make_data()
        self.data_builder.unmake_data()


class AbstractBuilder(metaclass=ABCMeta):

    def __init__(self, file_to_data, data_name):
        self.file_to_data = file_to_data
        self.data_name = data_name
        print('Data dumping...')

    @abstractmethod
    def make_data(self):
        pass

    @abstractmethod
    def unmake_data(self):
        pass


class Pickle(AbstractBuilder):

    def make_data(self):
        data_file = open(self.data_name, 'wb')
        pickle.dump(self.file_to_data, data_file)
        print(self.file_to_data + ' has been stored as ' + self.data_name)
        data_file.close()

    def unmake_data(self):
        data_file = open(self.data_name, 'rb')
        load_file = pickle.load(data_file)
        print(load_file)
        f = open(load_file, 'r')
        print(f.read())
        data_file.close()


class Shelf(AbstractBuilder):

    def make_data(self):
        s = shelve.open(self.data_name + '.db')
        try:
            s['key1'] = self.file_to_data
        finally:
            s.close()

    def unmake_data(self):
        s = shelve.open(self.data_name + '.db', flag='r')
        try:
            existing = s['key1']
        finally:
            s.close()
        print(existing)
