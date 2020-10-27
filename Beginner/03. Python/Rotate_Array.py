#Given an array, rotate the array to the right by k steps, where k is non-negative.

#Example 1
"""Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        le=len(nums)
        k=k%le
        k=le-k
        a=nums[:k]
        b=nums[k:]
        nums.clear()
        nums+=b+a
