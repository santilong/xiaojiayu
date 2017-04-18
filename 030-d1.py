import os
for each in os.listdir(os.curdir):
    size = os.path.getsize(each)
    print(each,'[',size,']')