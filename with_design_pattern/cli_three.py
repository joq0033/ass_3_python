from cmd import Cmd
from file_to_data import FileToData
from os import path
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import numpy as np
import cmd
import subprocess
from abstract import AbstractCli
from abstract import Context


class MyCliAdjunct(Cmd):
    def __init__(self):
        super().__init__()
        self.file_to_data = FileToData()

    # Harry's work
    def do_read_source_file(self, file_name):
        """This function extract data from the given python file to be an ast node.
        The file name should be [py_file_name.py]. The node will display as an indication of extraction"""
        try:
            if path.exists(file_name):
                self.file_to_data.read_file(file_name)
                print("The ast nodes below has been read from the given python file, " + file_name + ":")
                self.file_to_data.show_ast_nodes()
            else:
                print("Your given python file does not exist in the current directory ")
                print("or your input arguments were wrong. The input arguments ")
                print("should be [py_file_name.py]. ")
                print("Please try again!")
        except Exception as err:
            print("Please try again! The exception is: ", err)

    # Harry's work
    def help_read_source_file(self):
        print("\n".join(['Extract data from the given python file to be an ast node',
                         'Syntax: read_source_file [input source code file name.py]']))

    # Harry's work
    def do_validate_class_contents(self, file_name):
        """Validate, list and display class names, function names and the total numbers of them
        in the given python file. Class and function names are displayed in command line.
        Total numbers of classes and functions are displayed in a bar graph.
        Syntax: validate_class_contents [input source code file name.py]"""

        # sample: validate_class_contents test.py
        num_of_classes = 0
        num_of_functions = 0
        try:
            if path.exists(file_name):
                self.file_to_data.read_file(file_name)
                num_of_classes = len(self.file_to_data.tree.body)
                print("---There are " + str(num_of_classes) + " classes.-------------------")
                print("-----The classes are: -------------------")
                for my_class in self.file_to_data.tree.body:
                    print("-------" + my_class.name + " class")
                for my_class in self.file_to_data.tree.body:
                    print("---------The " + my_class.name + " class has " + str(len(my_class.body)) + " functions")
                    num_of_functions += len(my_class.body)
                    print("-----------The functions in " + my_class.name + " class are ")
                    for my_function in my_class.body:
                        print("---------------" + my_function.name + " function")
                print("total number of classes is " + str(num_of_classes))
                print("total number of functions is " + str(num_of_functions))
                # for my_function in my_class.body:
                #     if my_function.name == "__init__":
                #         print("---------The " + my_class.name + " class has " + str(
                #             len(my_function.body)) + " attributes")
                #         print("-----------The attributes in " + my_class.name + " class are ")
                #         for my_attribute in my_function.body:
                #             print("---------------" + my_attribute.targets[0].attr + " attribute")

                # types_x = ["class", "function"]
                # num_y = [num_of_classes, num_of_functions]
                # plt.plot(types_x, num_y, '-b', label="A simple line")
                # plt.legend(loc='upper left')
                # plt.title("Total Numbers of classes and functions")
                # plt.xlabel('Types')
                # plt.ylabel('Total Numbers')
                # plt.show()
                types_x = ["class", "function"]
                x_pos = np.arange(len(types_x))
                num_y = [num_of_classes, num_of_functions]
                plt.bar(x_pos, num_y, align='center', alpha=0.5)
                plt.xticks(x_pos, types_x)
                plt.ylabel('Total Numbers')
                plt.title('Total Numbers of classes and functions')
                plt.show()
            else:
                print("Your given python file does not exist in the current directory ")
                print("or your input arguments were wrong. The input arguments ")
                print("should be [py_file_name.py]. ")
                print("Please try again!")
        except Exception as err:
            print("Please try again! The exception is: ", err)

    # Harry's work
    def help_validate_class_contents(self):
        print("\n".join(['Validate, list and display class names, function names and the total numbers of them'
                         ' in the given python file.',
                         'Class and function names are displayed in command line.',
                         'Total numbers of classes and functions are displayed in a bar graph.',
                         'Syntax: validate_class_contents [input source code file name.py].']))

    # Harry's work
    def do_dot_2_png(self, input_dot_file_name):
        """Generate and display png file from the given dot file.
        Syntax: dot_2_png [input dot file name.dot]"""
        try:
            if path.exists(input_dot_file_name):
                dot_command = 'dot -Tpng ' + input_dot_file_name + ' -o ' + input_dot_file_name + '.png'
                subprocess.call(dot_command)
                print(input_dot_file_name + '.png ' + ' are done')
                png_file_name = input_dot_file_name + ".png"
                if path.exists(png_file_name):
                    # show png image
                    img = mpimg.imread(png_file_name)
                    fig = plt.imshow(img)
                    fig.axes.get_xaxis().set_visible(False)
                    fig.axes.get_yaxis().set_visible(False)
                    plt.show()
                else:
                    print("The image of class diagram cannot be generate.")
                    print("Please check with your system administrators.")
            else:
                print("Your given dot file does not exist in the current directory ")
                print("or your input arguments were wrong. The input arguments ")
                print("should be [dot_file_name.dot]. ")
                print("Please try again!")
        except Exception as err:
            print("Please try again! The exception is: ", err)

    # Harry's work
    def help_dot_2_png(self):
        """Help for dot_2_png command to generate and display png file from the given dot file.
                Syntax: dot_2_png [input dot file name.dot]"""
        print("\n".join(['Generate and display png file from the given dot file.',
                         'Syntax: dot_2_png [input dot file name.dot].']))


class MyCli(AbstractCli, MyCliAdjunct, Cmd):
    """Command line interpreter for generating UML class diagram"""

    # Harry's work
    def __init__(self, my_name=">"):
        Cmd.__init__(self, my_name)
        self.my_name = my_name
        self.prompt = ">>" + my_name + ">> "
        self.file_to_data = FileToData()

    def do_help(self, args):
        """Get help on commands"""
        cmd.Cmd.do_help(self, args)

    def do_diagram(self, file_names):
        """Generate and display a class diagram in png format from given [png_file_name_suffix py_file_name.py]"""
        self.file_names = file_names
        python_file_name = file_names[(file_names.find(" ") + 1):]
        png_file_name = 'classes_' + file_names[0:(file_names.find(" "))] + '.png'
        try:
            if path.exists(python_file_name):
                pyreverse_command = 'pyreverse -ASmn -o png -p ' + file_names
                subprocess.call(pyreverse_command)
                print(file_names + ' are done')

                if path.exists(png_file_name):
                    # show png image
                    img = mpimg.imread(png_file_name)
                    fig = plt.imshow(img)
                    fig.axes.get_xaxis().set_visible(False)
                    fig.axes.get_yaxis().set_visible(False)
                    plt.show()
                else:
                    print("The image of class diagram cannot be generate.")
                    print("Please check with your system administrators.")
            else:
                print("Your given python file does not exist in the current directory "
                      "or your input arguments were wrong. The input arguments "
                      "should be [png_file_name_suffix py_file_name.py]. "
                      "Please try again!")
        except Exception as err:
            print("Please try again! The exception is: ", err)

    # Harry's work
    def help_diagram(self):
        print("\n".join(['Generate and display a class diagram in png format from a given python file',
                         'Syntax: diagram [output png file name suffix] '
                         '[input source code file name.py])']))

    # Harry's work
    def do_exit(self, line):
        """Exit this command line interpreter"""
        print("Quitting......")
        return True

    # Harry's work
    def help_exit(self):
        print("\n".join(['Quit from this CLI', ':return: True']))


def main():
    cli = MyCli
    context = Context(cli)
    context.create_cli()


if __name__ == '__main__':
    cli_three = MyCli()
    cli_three.cmdloop()
