x = 0
numlist=[]
while x < 11:

    x+=1 
    numlist.append(x)

for num in numlist:
    if num == 5:
        continue
    print(num)