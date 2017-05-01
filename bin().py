def otb(n):
    result = ''
    if n:
        result = otb(n // 2)
        return result + str(n % 2)
    else:
        return result

print(otb(10))