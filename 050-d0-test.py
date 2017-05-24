import const
const.NAME = "FishC"
print(const.NAME)

try:
    const.NAME = 'FishC.com'
except TypeError as Err:
    print(Err)

try:
    const.name = 'FishC'
except TypeError as Err:
    print(Err)
