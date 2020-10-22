# move all the 0's in the end
# also maintain the order of non-zeros

def moveZeros(nums):
    j=0
    n = len(nums)
    # Move all the nonZero elements forward
    for num in nums:
       if(num!=0):
           nums[j] = num
           j+=1
    # now at this point j is index of first zero
    for x in range(j, n):
        nums[x] = 0

    return nums
nums = [7, 2, 6, 0, 9, 1, 0]
ans = moveZeros(nums)
print(ans)