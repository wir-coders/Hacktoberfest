def search(arr, n, k): 

	for i in range (0, n): 
		if (arr[i] == k): 
			return i+1;             #to take index from 1 rather than 0
	return -1; 

T = int(input())
for j in range(T):
    
    n,k=map(int, input().split())

    arr = [int(i) for i in input().split()]
   
    
   
    result = search(arr, n, k) 
    if(result == -1): 
    	print("-1") 
    else: 
    	print (result); 
