nums = [1,3,5,6]
target = 7

if target > nums[-1]:
    print(len(nums))
else:
    for ind, num in enumerate(nums):
        if target > num and target <= nums[ind+1]:
            print(ind+1)

class Solution:
    def searchInsert(self, nums, target):
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums) 
        for ind, num in enumerate(nums):
            if target > num and target <= nums[ind+1]:
                return ind+1