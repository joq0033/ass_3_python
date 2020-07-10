from cmd import Cmd
import DiagramCreator
from abstract import AbstractCli
import SQLDatabase
from abstract import Context
from PickleMaker import MyPickle


class MyPromptAdjunct(Cmd, object):

    def do_pickle(self, inp):
        MyPickle(inp, input('name of pickle file: ')).make_data()

    def help_pickle(self):
        print('pickle [filename], enter file to pickle then the name of the pickle file')

    def do_unpickle(self, inp):  # i don't know if this is correct or not
        MyPickle('a', inp).unmake_data()

    def help_unpickle(self):
        print('unpickle [picklefilename], enter the name of a file that has been pickled')

    def do_createtable(self, inp):
        SQLDatabase.MyDatabase().create_table(inp)

    def help_createtable(self):
        print('a')

    def do_addtotable(self, inp):
        f_number = input('File number: ')
        try:
            val = int(f_number)
            SQLDatabase.MyDatabase().add_data(inp, val, input('File name: '), input('File content: '))
        except ValueError:
            print('Please input a integer!')

    def help_addtotable(self):
        print('b')

    def do_showtable(self, inp):
        SQLDatabase.MyDatabase().show_data(inp)

    def help_showtable(self):
        print('a')

    def do_deletetable(self, inp):
        SQLDatabase.MyDatabase().delete_table(inp)

    def help_deletetable(self):
        print('b')

    def default(self, inp):
        print(inp + ' is an incorrect command. Type ? to list commands.')


class MyPrompt(AbstractCli, MyPromptAdjunct, Cmd, object):
    prompt = '> '
    intro = "Type ? to list commands"

    def do_exit(self, inp):
        print('Exiting Program...')
        return True

    def do_help(self, args):
        """Get help on commands"""
        Cmd.do_help(self, args)

    def help_exit(self):
        print('Exit the application.')

    def do_diagram(self, inp):
        image_name = input('Image name/type:')
        DiagramCreator.MyCreator(image_name, inp).create_diagram()

    def help_diagram(self):
        print('Create a class diagram. Enter file location of py/dot file, then enter name/type of image.')

    do_EOF = do_exit
    help_EOF = help_exit


def main():
    cli = MyPrompt
    context = Context(cli)
    context.create_cli()


if __name__ == '__main__':
    MyPrompt().cmdloop()
