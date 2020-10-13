'''
Given an input of a 2D array of integers, removes all duplicates from the array.
Empty sub-arrays are removed.
'''
map = {}

def remove_duplicates(all_nums):
    end_index = len(all_nums) #length of all_nums
    i = 0 #current index of all_nums
    while(i < end_index):
        j = 0 #current index of sub-array
        sub_arr = all_nums[i]
        sub_end = len(sub_arr)
        while(j < sub_end):
            if(map.get(sub_arr[j]) != None):
                sub_end = sub_end - 1 #decrease length of sub_arr due removal
                sub_arr.remove(sub_arr[j])
                if(len(all_nums[i]) == 0):
                    end_index = end_index - 1 #decrease length of all_nums due to empty array removal
                    all_nums.remove(all_nums[i])
                    i = i - 1
                continue
            else:
                print("No",sub_arr[j],"found in map.")
                map[sub_arr[j]] = 1
            j = j + 1
        i = i + 1

    print(all_nums)

arr = [[1, 2], [2, 2, 2, 2, 2], [2, 3], [4, 5, 2, 2, 2], [3, 3, 3, 4]]

remove_duplicates(arr)
