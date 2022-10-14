class Base:
    def foo(self):
        return self.bar()

    def __init_subclass__(self):
        assert "bar" in vars(self), "Derived messed up!"
        return super().__init_subclass__()


class Derived(Base):
    assert hasattr(Base, "foo"), "Base messed up!"
    
    def bar(self):
        return "bar"

