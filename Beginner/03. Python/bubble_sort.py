# bubble sort

def bubble_sort(array):
  for i in range(len(array) - 1):
    for j in range(len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j + 1]
        array[j + 1] = temp
  return array

array = [2, 3, 5, 4, 1]
print(bubble_sort(array))
