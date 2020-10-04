def binary( arr, l, r, x):

    if(r >= l):
        mid = int((l + r)/2)            #int is taken here as by default python would take float, don't do l+(r-l)/2 it can overflow
        if(arr[mid] == x):
            return mid
        elif(arr[mid] > x):
            return binary(arr, l, mid-1, x)
        else:
            return binary(arr, mid+1, r, x)
    else:
        return 0
       
      
#for input type
#2
#3 5
#1 4 5
#3 3
#2 8 7
       



for _ in range(int(input())):
    
    n,k = map(int, input().split())       #will print in same line with space
    
    # print(n,k)
    arr = list(map(int, input().split()))       #standard way no boundary
   
    result = binary(arr, 0, len(arr)-1, k) 
    if(result == 0): 
         print("-1") 
    else: 
        print(result+1)                          #index will start from 1 rather than 0

