#Bubble Sort
def bubbleSort(array):
    #the outer loop will traverse through all the element starting from the 0th index to n-1
    for i in range(0, len(array)-1):
        #the inner loop will traverse through all elements except the last element as it is sorted and is in a fixed position
        for j in range(0, len(array) - 1 - i):
            #if the current element is found greater than the next element
            if array[j] > array[j+1]:
                #then swap the position of the two elements
                array[j],array[j+1] = array[j+1], array[j]
                
#taking input from user separated by delimiter                
inp = input('Enter a list of numbers separated by commas: ').split(',')
#typecasting each value of the list into integer
array = [int(num) for num in inp]
bubbleSort(array)
print('The Sorted list is :',array)
