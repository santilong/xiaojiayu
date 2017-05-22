class RY:
    def __init__(self, end=2017):
        self.start = 0
        self.end = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.end:
            if (self.start%4 == 0 and self.start%100 != 0) or (self.start%400 == 0):
                print(str(self.start) + '是闰年')
            else:
                print(str(self.start) + '不是闰年')
                

