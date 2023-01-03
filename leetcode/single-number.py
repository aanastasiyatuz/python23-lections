nums = [2,2,1]
unique = []

for i in nums:
    if i in unique:
        unique.remove(i)
        continue
    unique.append(i)
print(unique[0])

class Solution:
    def singleNumber(self, nums):
        unique = []

        for i in nums:
            if i in unique:
                unique.remove(i)
                continue
            unique.append(i)
        return unique[0]