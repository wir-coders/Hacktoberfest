def partition(arr,low,high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low,high):
        
        if arr[j] < pivot:                                             # If current element is smaller than the pivot 
            i = i+1                                                    # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    return(i+1)
    
    
def quickSort(arr, low, high):
    if (low < high):
        pi = partition(arr, low, high)
            
        quickSort(arr, low, pi-1)                               # Separately sort elements before partition and after partition 
        quickSort(arr, pi+1, high)
        
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
    
