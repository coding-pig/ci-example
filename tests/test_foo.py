from src import foo


class TestFoo:

    def test_name(self):
        f = foo.Foo('a')
        assert f.name == 'a'
