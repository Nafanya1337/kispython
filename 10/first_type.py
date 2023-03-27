# Первый тип - где есть тупик

class MyClass:
    def __init__(self):
        self.state = 'A'

    def visit(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            return 4
        if self.state == 'D':
            self.state = 'B'
            return 6
        if self.state == 'E':
            self.state = 'B'
            return 8
        if self.state == 'F':
            self.state = 'G'
            return 9
        raise MealyError('visit')

    def pan(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 7
        raise MealyError('pan')


class MealyError(Exception):
    pass


def main():
    return MyClass()


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.visit() == 0  # 1
    assert o.pan() == 2  # 2
    assert o.visit() == 4  # 4
    assert o.pan() == 3  # 3
    assert o.visit() == 6  # 6
    assert o.pan() == 2  # 2
    assert o.pan() == 3  # 3
    assert o.pan() == 5  # 5
    assert o.pan() == 7  # 7
    assert o.visit() == 9  # 9
    raises(lambda: o.visit(), MealyError)
    raises(lambda: o.pan(), MealyError)
    o = main()
    assert o.pan() == 1  # 1
    assert o.pan() == 3  # 3
    assert o.pan() == 5  # 5
    assert o.visit() == 8  # 8


test()
