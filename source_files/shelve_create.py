import shelve


class Shelf:
    def __init__(self, file_to_shelf, shelf_name):
        self.file_to_shelf = file_to_shelf
        self.shelf_name = shelf_name

    def make_shelf(self):
        s = shelve.open(self.shelf_name + '.db')
        try:
            s['key1'] = self.file_to_shelf
        finally:
            s.close()

    def existing_shelf(self):
        s = shelve.open(self.shelf_name + '.db', flag='r')
        try:
            existing = s['key1']
        finally:
            s.close()
        print(existing)
