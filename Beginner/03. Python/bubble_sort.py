#Bubble sort
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
arr = [74, 36, 15, 92, 10, 47, 82] 
bubbleSort(arr) 
print ("Sorted array is:") 
for i in arr: 
    print (i,end=" ")
