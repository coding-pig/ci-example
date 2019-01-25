from foo import Foo

class TestFoo:

    def test_name(self):
        foo = Foo('a')
        assert foo.name == 'a'
