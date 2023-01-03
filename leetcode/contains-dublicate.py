nums = [1,2,3,1, 2, 3, ]
unique = []

for num in nums:
    print(num, unique)
    if num in unique:
        print(True)
        break
    unique.append(num)

class Solution:
    def containsDuplicate(self, nums):
        unique = []

        for num in nums:
            if num in unique:
                return True
            unique.append(num)