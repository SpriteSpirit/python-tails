class PrintInfoMixin:
    def __repr__(self):
        attrs = [f"{key}={value}" for key, value in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(attrs)})"
