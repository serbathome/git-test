
class SomeTestClass:
    def __init__(self):
        self.version = 1
    def __str__(self):
        return str(self.version)

a = SomeTestClass()
print(a)
