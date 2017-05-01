# def huiwen(len(n)):
#     flag = 1
#     if len(n)//2:
#         huiwen(len(n)//2)
#         if n[len(n)//2-1] == n[len(n)//2+1]:
#             return flag = 1
#     else:
#         return flag = 0

def is_palindrome(n, start, end):
    if start > end:
        return 1
    else:
        return is_palindrome(n, start + 1, end - 1) if n[start] == n[end] else 0


string = input('请输入一串字符串：')
length = len(string) - 1

if is_palindrome(string, 0, length):
    print('\"%s\"是回文字符串!' % string)
else:
    print('\"%s\"不是回文字符串!' % string)




