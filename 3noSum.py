def find3Numbers(A, n, x): 

	for i in range( 0, n-2): 
		
		for j in range(i + 1, n-1): 
		 
			for k in range(j + 1, n): 
			    
				if A[i] + A[j] + A[k] == x: 
					#print("Triplet is", A[i], ", ", A[j], ", ", A[k])       #to get the elements in triplet
					return True
	return False
	
  
T = int(input())
for _ in range(T):
    
    n,x = map(int, input().split())           #x is the sum of which triplet is to be found
    
    A = [int(i) for i in input().split()]
    
    result = find3Numbers(A, n, x)
    if(result == True):
        print("1")
    else:
        print("0")
