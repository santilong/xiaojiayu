class Calc(int):
    def __new__(cls,var):
        if isinstance(var, str):
            total = 0
            for each in var:
                total += ord(each)
            ppp = total
        else:
            ppp = var
        return int.__new__(cls, ppp)

print(Calc(123))
print(Calc('A'))

# class Nint(int):
#     def __new__(cls, arg=0):
#         if isinstance(arg, str):
#             total = 0
#             for each in arg:
#                 total += ord(each)
#             arg = total
#         return int.__new__(cls, arg)
#
# print(Nint(123))
# print(Nint('A'))
