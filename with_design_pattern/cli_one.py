import os
import cmd
import subprocess
import shlex
import os.path
from abstract import AbstractCli
from abstract import Context
from shelve_create import Shelf


class CliAdjunct(cmd.Cmd, object):

    def do_check_dot(self, classes_result):
        """Checks if dot file exists"""
        try:
            if os.path.exists(classes_result):
                print(classes_result + ' is ready to be converted')
            else:
                message = "the dot file does not exist"
                raise NameError(message)

        except NameError as e:
            print(e)

    def help_check_dot(self):
        message = 'Checks if dot file exists. Example: check_dot classes_result.dot'
        print(message)

    def do_dot(self, classes_result):
        """Turn dot file into png file."""
        try:
            if os.path.exists(classes_result):
                args = shlex.split(' -Tpng -O classes_result.dot')
                subprocess.call(['dot'] + args)
                print('the conversion is done')

            else:
                message = "the dot file failed to be converted to png.."
                print(message)

        except Exception as err:
            print("Failed, the error is: ", err)

    def help_dot(self):
        message = 'Turn dot file into png file. Example: dot classes_result.dot'
        print(message)

    def do_shelve(self, inp):
        """Create shelf!"""
        Shelf(inp, input('name of file to shelf: ')).make_data()

    def help_shelve(self):
        message = 'make_shelve then press enter, then enter the name of the file shelved [example: cli.py]'
        print(message)

    def do_unshelve(self, inp):
        """Access data!"""
        Shelf(inp, input('name of shelf file to access: ')).unmake_data()

    def help_unshelve(self):
        message = 'existing_shelve then press enter, then enter the name of the shelved file to access'
        print(message)


class Cli(AbstractCli, CliAdjunct, cmd.Cmd, object):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">>> "
        self.intro = "Welcome to commands! Type help."
        self.__setCanExit(True)

    def __canExit(self):
        return self.canExit

    def __setCanExit(self, value):
        self.canExit = value

    # The do's
    def do_exit(self, args):
        """Exits from the console"""
        if self.__canExit():
            return True
        print("Please, wait until all operations end")
        return False

    def help_exit(self):
        message = 'Quit interface.'
        print(message)

    def do_help(self, args):
        """Get help on commands"""
        cmd.Cmd.do_help(self, args)

    def do_diagram(self, source_file):
        """Generate dot file."""
        try:
            if os.path.exists(source_file):
                args = shlex.split('-o dot -p result source_file.py')
                subprocess.call(['pyreverse'] + args)
                print('Dot File is ready please check folder.')
            else:
                message = "Process has failed."
                raise NameError(message)

        except NameError as e:
            print(e)

    def help_diagram(self):
        message = 'Make source py file into dot file. Example: diagram source_file.py'
        print(message)


def main():
    cli = Cli
    context = Context(cli)
    context.create_cli()


if __name__ == '__main__':
    console = Cli()
    console . cmdloop()
