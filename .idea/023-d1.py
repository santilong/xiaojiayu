list1 = []
def get_digits(n):
    if n:
        get_digits(n // 10)
        return list1.append(n % 10)
    else:
        return list1
get_digits(12345)
print(list1)

###小甲鱼答案：
# result = []
# def get_digits(n):
#         if n > 0:
#                 result.insert(0, n%10)
#                 get_digits(n//10)
#
# get_digits(12345)
# print(result)

