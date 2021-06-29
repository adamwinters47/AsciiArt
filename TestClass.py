class TestClass:
    def __init__(self, name):
        self.__set_name__(name)

    def print_name(self):
        return f'Test class is named {self.get_name()}'

    def __set_name__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name