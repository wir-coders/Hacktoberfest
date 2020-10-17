def maxSum(arr, windowSize):
    arrSize = len(arr)
    if(arrSize<windowSize):
        print("Invalid operation")
        return -1
        
    # finding sum of the first window
    window_sum = sum(arr[i] for i in range(windowSize))
    max_sum = window_sum

    for i in range(arrSize-windowSize):
        window_sum = window_sum-arr[i] + arr[i+windowSize]
        max_sum = max(window_sum, max_sum)
    
    return window_sum
    

arr = [80, -50, 90, 100]
k=2
answer = maxSum(arr, k)
print("Max sum of %d consecutive elements: %d"%(k, answer))