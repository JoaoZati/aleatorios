import inspect


class MyClass(object):
    # MyClass property
    property1 = [1, 2, 3]

    def __init__(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = a

    def add(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state + a
        return self.state

    def subtract(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state - a
        return self.state

    def multiply(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state * a
        return self.state

    def divide(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state / a
        return self.state

    @staticmethod
    def global_method(a, b):
        return a + b

    @classmethod
    def myclass_method(cls):
        return cls


if __name__ == '__main__':
    print('Methods List:')
    method_list = [attribute for attribute in dir(MyClass)
                   if callable(getattr(MyClass, attribute)) and attribute.startswith('__') is False]
    print(method_list)
    print('Atributes List')
    method_list = [attribute for attribute in dir(MyClass)
                   if not callable(getattr(MyClass, attribute)) and attribute.startswith('__') is False]
    print(method_list)
    print('Methods List using inspect:')
    method_list = inspect.getmembers(MyClass, predicate=inspect.ismethod)
    print(method_list)
