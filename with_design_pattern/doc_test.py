"""
>>> from cli_one import Cli
>>> co = Cli()
>>> co.do_help('help')
Get help on commands
>>> co.help_diagram()
Make source py file into dot file. Example: diagram source_file.py
>>> co.help_exit()
Quit interface.
>>> co.do_exit('exit')
True

>>> from cli_two import MyPrompt
>>> co = MyPrompt()
>>> co.do_help('help')
Get help on commands
>>> co.help_diagram()
Create a class diagram. Enter file location of py/dot file, then enter name/type of image.
>>> co.help_exit()
Exit the application.
>>> co.do_exit('exit')
Exiting Program...
True

>>> from cli_three import MyCli
>>> co = MyCli()
>>> co.do_help('help')
Get help on commands
>>> co.help_diagram()
Generate and display a class diagram in png format from a given python file
Syntax: diagram [output png file name suffix] [input source code file name.py])
>>> co.help_exit()
Quit from this CLI
:return: True
>>> co.do_exit('exit')
Quitting......
True

>>> from PickleMaker import MyPickle
>>> pm = MyPickle('DoctestPickleFile.py','test')
Data dumping...
>>> pm.make_data()
DoctestPickleFile.py has been stored as test
>>> pm.unmake_data()
DoctestPickleFile.py
testfile = 1
<BLANKLINE>

>>> from shelve_create import Shelf
>>> sc = Shelf('file_to_data', 'data_name')
Data dumping...
>>> sc.make_data()
>>> sc.unmake_data()
file_to_data
"""

import doctest


def test1():
    return doctest.testmod(verbosity=2)


if __name__ == '__main__':
    doctest.testmod()
