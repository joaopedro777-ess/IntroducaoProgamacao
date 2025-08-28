pos=0
neg=0
for i in range(20):
    n = int(input())
    if n > 0:
        pos+=i
    else:
     neg+=1

print(pos,neg)