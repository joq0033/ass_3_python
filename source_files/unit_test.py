import unittest
from cli_one import Cli
from cli_two import MyPrompt
from cli_three import MyCli


class TestCliOne(unittest.TestCase):

    def setUp(self):
        self.cliOne = Cli()

    def test_do_diagram(self):
        raised = True
        try:
            self.cliOne.do_diagram('diagram source_file')
        except:
            raised = False
        self.assertTrue(raised, 'Error Raised')


class TestCliTwo(unittest.TestCase):

    def setUp(self):
        self.cliTwo = MyPrompt()

    def test_do_diagram(self):
        raised = True
        try:
            self.cliTwo.do_diagram('diagram source_file')
        except:
            raised = False
        self.assertTrue(raised, 'Error Raised')


class TestCliThree(unittest.TestCase):

    def setUp(self):
        self.cliThree = MyCli()

    def test_do_diagram(self):
        raised = True
        try:
            self.cliThree.do_diagram('diagram test source_file.py')
        except:
            raised = False
        self.assertTrue(raised, 'Error Raised')


if __name__ == '__main__':
    unittest.main()
