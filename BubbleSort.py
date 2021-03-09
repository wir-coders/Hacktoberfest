def bubble(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            
            if arr[j] > arr[j+1]:
                
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
            if swapped == False:
                break
            
T = int(input())
for i in range(T):
    
    n = int(input())
    arr = [int(i) for i in input().split()]
   
    bubble(arr) 
   
    print() 
    for i in range(len(arr)): 
        print ("%d" %arr[i],end=" ") 
  
