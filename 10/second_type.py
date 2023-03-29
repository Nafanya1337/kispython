# Второй тип - нет тупика

class MyClass:
    def __init__(self):
        self.state = 'A'

    def trace(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'D':
            self.state = 'G'
            return 4
        if self.state == 'E':
            self.state = 'B'
            return 7
        raise MealyError('trace')

    def melt(self):
        if self.state == 'C':
            self.state = 'D'
            return 2
        if self.state == 'D':
            self.state = 'E'
            return 3
        if self.state == 'E':
            self.state = 'A'
            return 6
        if self.state == 'F':
            self.state = 'G'
            return 8
        if self.state == 'G':
            self.state = 'B'
            return 9
        raise MealyError('melt')

    def mass(self):
        if self.state == 'E':
            self.state = 'F'
            return 5
        raise MealyError('mass')


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
    assert o.trace() == 0
    assert o.trace() == 1
    assert o.melt() == 2
    assert o.melt() == 3
    assert o.melt() == 6
    try:
        raises(lambda: o.trace(), MealyError)
    except AssertionError as e:
        pass
    raises(lambda: o.melt(), MealyError)
    raises(lambda: o.mass(), MealyError)
    o = main()
    assert o.trace() == 0
    assert o.trace() == 1
    assert o.melt() == 2
    assert o.melt() == 3
    assert o.trace() == 7
    try:
        raises(lambda: o.trace(), MealyError)
    except AssertionError as e:
        pass
    try:
        raises(lambda: o.melt(), MealyError)
    except AssertionError as e:
        pass
    raises(lambda: o.mass(), MealyError)
    o = main()
    assert o.trace() == 0
    assert o.trace() == 1
    assert o.melt() == 2
    assert o.melt() == 3
    assert o.mass() == 5
    assert o.melt() == 8
    assert o.melt() == 9
    assert o.trace() == 1
    assert o.melt() == 2
    assert o.trace() == 4
    raises(lambda: o.trace(), MealyError)
    try:
        raises(lambda: o.melt(), MealyError)
    except AssertionError as e:
        pass
    raises(lambda: o.mass(), MealyError)


test()
