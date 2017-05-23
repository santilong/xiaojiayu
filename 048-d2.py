class MyRev():
    def __init__(self, var):
        self.data = var
        self.index = len(var)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]









