from abc import ABC, abstractmethod


class Context(object):

    def __init__(self, strategy):
        self.strategy = strategy

    def create_cli(self):
        self.strategy.do_exit()
        self.strategy.help_exit()
        self.strategy.do_help()
        self.strategy.do_diagram()
        self.strategy.help_diagram()


class AbstractCli(ABC):

    @abstractmethod
    def do_exit(self, args):
        pass

    @abstractmethod
    def help_exit(self):
        pass

    @abstractmethod
    def do_help(self, args):
        pass

    @abstractmethod
    def do_diagram(self, source_file):
        pass

    @abstractmethod
    def help_diagram(self):
        pass
