def find3Numbers(A, n, x): 
    
    A.sort()
    for i in range(0,n-2):
        
        l = i + 1
        
        r = n-1 
        
        while (l < r):
            if(A[i] + A[l] + A[r] == x):
                return True
            elif (A[i] + A[l] + A[r] < x):
                l += 1
            else:
                r -= 1
    return False
	
T = int(input())
for _ in range(T):
    
    n,x = map(int, input().split())
    
    A = [int(i) for i in input().split()]
    result = find3Numbers(A, n, x)
    if(result == True):
        print("1")
    else:
        print("0")
        
        
        
        
    
    
    
    












        
        



