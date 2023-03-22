class SomeClass:
    def __init__(self):
	self.version = "0"
    def __str__(self):
	return self.version


o = SomeClass()
print(o)
