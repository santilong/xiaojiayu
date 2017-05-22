class NewList:
    def __init__(self, *args):
        self.value = [x for x in args]
        self.count = {}.fromkeys(range(len(self.value)), 0)

    def __len__(self):
        return len(self.value)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value

    def __delitem__(self, key):
        del self.value[key]
        del self.count[key]

    def append(self, var):
        self.value.append(var)
        self.count[len(self.count)] = 0

    def pop(self):
        self.value.pop()
        self.count.pop(list(self.count.keys())[-1])

    def remove(self,var):
        self.index = self.value.index(var)
        self.value.remove(var)
        self.count.pop(self.index)

    def clear(self):
        self.value.clear()
        self.count.clear()

    # def insert(self, index,var):
    #     if len(self.value) <= index:
    #         self.value.insert(index, var)
    #         self.count[len(self.count)] = 0
    #     else:
    #         self.value.insert(index,var)










