math=[]
total=0
high=0
low=100
n=int(input('How many people in this classs?'))
for i in range(n):
    stuname = input('Name:')
    score = int(input('please input the score:'))
    total = total+score
    math.append(stuname)
    math.append(score)
for i in range(1,n*2,2):
    if math[i] > high:
        high = math[i]
        highname = math[i-1]
for i in range(1,n*2,2):
    if math[i] < low:
        low = math[i]
        lowname = math[i-1]       
average = total / n
print(math)
print('average:',average)
print('high:',high,highname)
print('low:',low,lowname)   