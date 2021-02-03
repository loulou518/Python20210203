math=[]
name = []
total=0
high=0
low=100
n=int(input('How many people in this classs?'))
for i in range(n):
    stuname = input('Name:')
    score = int(input('please input the score:'))
    total = total+score
    name.append(stuname)
    math.append(score)
for i in range(n):
    if math[i] > high:
        high = math[i]
        highname = name[i]
for i in range(n):
    if math[i] < low:
        low = math[i]
        lowname = name[i]       
average = total / n
print(math)
print('average:',average)
print('high:',high,highname)
print('low:',low,lowname)  