name = list()
score = list()
def average(score):
    total = 0
    for i in range(len(score)):
        total = total+score[1]
        ave = total / len(score)
        return ave
def highest(score,name):
    high = 0
    temp = []
    for i in range(len(score)):
          if score[i] > high:
             high = score[i]
             highname = name[i]
    temp.append(highname)
    temp.append(high)
    return temp
def lowest(score,name):
    low=100
    temp = []
    for i in range(len(score)):
        if score[i] < low:
            low = score[i]
            lowname = name[i]
    temp.append(lowname)
    temp.append(low)
    return temp

pepople=int(input('How many people in this classs?'))
for i in range(pepople):
     n = input('Name:')
     name.append(n)
     s = int(input('please input the score:'))
     score.append(s)
print(name)
print(score)
a = average(score)
hi = highest(score,name)
lo = lowest(score,name)
print(a)
print(hi[0],'got the highest scores',hi[1])
print(lo[0],'got the highest scores',lo[1])