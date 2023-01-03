digits = [1,2,3]

string_number = ''
for digit in digits:
    string_number = string_number + str(digit)

res_number = int(string_number) + 1
res_list = []

for i in str(res_number):
    res_list.append(int(i))

print(res_list)

class Solution:
    def plusOne(self, digits):
        string_number = ''
        
        for digit in digits:
            string_number = string_number + str(digit)

        res_number = int(string_number) + 1
        res_list = []

        for i in str(res_number):
            res_list.append(int(i))

        return res_list