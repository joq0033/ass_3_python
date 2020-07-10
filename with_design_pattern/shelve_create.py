import shelve
from abstract import AbstractSerializer


class Shelf(AbstractSerializer):

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
