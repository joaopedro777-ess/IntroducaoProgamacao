thanos=1,5
spider=1,1
anos=0
for i in range (1000000): 
    thanos += 0,2
    spider += 0,3
    if spider>thanos:
        break
    else:
        anos +=1
print(anos)