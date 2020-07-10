import pickle
from abstract import AbstractSerializer


class MyPickle(AbstractSerializer):

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
