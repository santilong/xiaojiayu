<<<<<<< HEAD
import pickle
def recordfile(girlcontent,boycontent,count):
    # count = 1
    while count <= 3:
        boyfile = open('boy_' + str(count) + '.txt','wb')
        girlfile = open('girl_' + str(count) + '.txt','wb')
        pickle.dump(girlcontent,girlfile)
        pickle.dump(boycontent,boyfile)
        boyfile.close()
        girlfile.close()
        girlcontent = []
        boycontent = []
def createlist():
    f = open('record.txt','r',encoding='cp936')
    girlcontent = []
    boycontent = []
    count = 1
    for each in f:
        if each[0:5] != '=====':
            role,content = each.split(':',maxsplit=1)
            if role == '小客服':
                girlcontent.append(content)
            elif role == '小甲鱼':
                boycontent.append(content)
        elif each[0:5] == '=====':
            recordfile(girlcontent, boycontent,count)
        elif each == '':
            recordfile(girlcontent, boycontent,count)
    count += 1

def readbin():
    count = 1
    boylist = []
    girllist = []
    while count <= 3:
        boy = open('boy_' + str(count) + '.txt','rb')
        girl = open('girl_' + str(count) + '.txt','rb')
        boylist.append(pickle.load(boy))
        girllist.append(pickle.load(girl))
        count += 1
    print(boylist)

createlist()
# readbin()

=======
import pickle
def recordfile(girlcontent,boycontent,count):
    boyfile = open('boy_' + str(count) + '.txt','wb')
    girlfile = open('girl_' + str(count) + '.txt','wb')
    pickle.dump(girlcontent,girlfile)
    pickle.dump(boycontent,boyfile)
    boyfile.close()
    girlfile.close()

def createlist():
    f = open('record.txt','r',encoding='cp936')
    girlcontent = []
    boycontent = []
    count = 1
    for each in f:
        if each[0:5] != '=====':
            role,content = each.split(':',maxsplit=1)
            if role == '小客服':
                girlcontent.append(content)
            elif role == '小甲鱼':
                boycontent.append(content)
        elif each[0:5] == '=====':
            recordfile(girlcontent, boycontent,count)
            count += 1
            girlcontent = []
            boycontent = []
            continue
        recordfile(girlcontent,boycontent,count)
    count += 1

def readbin():
    count = 1
    boylist = []
    girllist = []
    while count <= 3:
        boy = open('boy_' + str(count) + '.txt','rb')
        girl = open('girl_' + str(count) + '.txt','rb')
        boylist.append(pickle.load(boy))
        girllist.append(pickle.load(girl))
        count += 1
    print(boylist)
    print(girllist)

# createlist()
readbin()

>>>>>>> 63aeea4d4ec93c10634f1bdfa1381e122615658c
