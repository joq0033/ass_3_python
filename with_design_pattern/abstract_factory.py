from abc import ABC, abstractmethod
from PickleMaker import *
from shelve import *


class AbstractSerializerFactory(ABC):
    """
        The Abstract Factory interface declares a set of methods that return
        different abstract products. These products are called a family and are
        related by a high-level theme or concept. Products of one family are usually
        able to collaborate among themselves. A family of products may have several
        variants, but the products of one variant are incompatible with products of
        another.
    """
    @abstractmethod
    def create_serializer(self):
        pass


class ConcretePickleFactory(AbstractSerializerFactory):
    """
        Concrete Factories produce a family of products that belong to a single
        variant. The factory guarantees that resulting products are compatible. Note
        that signatures of the Concrete Factory's methods return an abstract
        product, while inside the method a concrete product is instantiated.
    """
    def create_serializer(self):
        return MyPickle('DocTestPickle.py', 'test')


class ConcreteShelfFactory(AbstractSerializerFactory):
    """
        Concrete Factories produce a family of products that belong to a single
        variant. The factory guarantees that resulting products are compatible. Note
        that signatures of the Concrete Factory's methods return an abstract
        product, while inside the method a concrete product is instantiated.
    """
    def create_serializer(self):
        return Shelf('source_file')


def test_serializers(factory):
    """
        The client code works with factories and products only through abstract
        types: AbstractFactory and AbstractProduct. This lets you pass any factory
        or product subclass to the client code without breaking it.
    """
    serialize = factory.create_serializer()
    serialize.make_data()
    serialize.unmake_data()


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type: MyPickle")
    test_serializers(ConcretePickleFactory())
