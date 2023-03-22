
class SomeTestClass:
    def __init__(self):
        self.version = 1
    def __str__(self):
        return str(self.version)

class SomeClass:
    def __init__(self):
	self.version = "0"
    def __str__(self):
	return self.version

a = SomeTestClass()
print(a)
o = SomeClass()
print(o)

