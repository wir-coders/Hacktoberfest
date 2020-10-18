#Python code to demonstrate prefix sum algorithm.

def prefix_sum(arr):
	pref = [0]*(len(arr)+1)     #Create a prefix sum array of length (n+1)
	pref[0] = arr[0]             #initialise its first element with that of the given array's first element
	for i in range(1, len(arr)):
		pref[i] = pref[i-1] + arr[i]        #keep adding the previous element's prefix sum to the current element
	return pref

array = list(map(int, input().split()))
print(prefix_sum(array))
