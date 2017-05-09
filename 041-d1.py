class C2F(float):
    def __new__(cls,c):
        return float.__new__(cls,c * 1.8 + 32)


c2f = C2F('32')