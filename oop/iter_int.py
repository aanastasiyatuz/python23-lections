class IterInt(int):
    def __iter__(self):
        for i in str(self):
            yield int(i)

    def __getitem__(self, index):
        res = str(self)[index]
        return int(res)

    def __len__(self):
        count = 0
        for i in self:
            count += 1
        return count
        # return len(str(self))

    def __add__(self, other):
        new_num = super().__add__(other)
        return IterInt(new_num)

iter_num = IterInt(67545789)

for i in iter_num:
    print(i * 2)

print(iter_num[1:5])

print(len(iter_num))

new_num = iter_num + 10
for i in new_num:
    print(i)
