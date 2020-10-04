#to check that a T is formed or not by given coordinates of x and y

#Test case : 1 
# 7 5
# 8 5
# 6 5
# 7 6
# 7 7

#O/P YES




for t in range(int(input())):
    a=[]
    x=[]
    y=[]
    xcount=[]
    ycount=[]
        
    for _ in range(5):
        
        i,j = (list(map(int,input().split())))
        x.append(i)
        y.append(j)
        
    for i in set(x):
        
        xcount.append(x.count(i))
        
    for j in set(y):
        
        ycount.append(y.count(j))
        
    x = sorted(list(set(x)))
    y = sorted(list(set(y)))
    
    if 3 not in xcount or 3 not in ycount or x[1]- x[0]!= 1 or x[2]- x[1]!= 1 or y[1]- y[0]!= 1 or y[2]- y[1]!= 1:
        print("No")
    else:
        print("Yes")
