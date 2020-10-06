# Creating a function for binary search
def binary_search(array, ele):
    # defining the two pointers

    low = 0
    high = len(array)-1

    while(low <= high):
        # finding mid
        mid = (low+(high-low)//2)

        # comparing element with the middle value of array
        if array[mid] == ele:
            return mid

        elif array[mid] > ele:
            high = mid-1

        else:
            low = mid+1

    # if we are here we surely did not find the element
    return -1

# Driver Code


# taking inputs
array = list(
    map(int, input("Enter numbers in space separated sorted form").split()))
element = int(input("Enter the element to search"))

# fetching the answer from our function
index = binary_search(array, element)

if index == -1:
    print("Sorry could not find this element")
else:
    print(f'Element found at {index+1} position')
