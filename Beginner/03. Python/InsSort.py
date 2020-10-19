#Insertion Sort
def insertionSort(ar):
    #the outer loop starts from 1st index as it will have at least 1 element to compare itself with
    for i in range(1, len(ar)):
        
        #making elements as key while iterating each element of i
        key = ar[i]
        #j is the element left to i
        j = i - 1
        #checking condition
        while j>=0 and key<ar[j]:
            ar[j+1] = ar[j]
            j = j - 1
        ar[j+1] = key
        
#taking input from user separated by delimiter                
inp = input('Enter a list of numbers separated by commas: ').split(',')
#typecasting each value of the list into integer
ar = [int(num) for num in inp]
insertionSort(ar)
print('The Sorted list is :',ar)
