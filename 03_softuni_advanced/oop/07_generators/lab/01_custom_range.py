class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current <= self.end:
            return self.current
        # self.current = self.start - 1
        raise StopIteration


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)

# for num in one_to_ten:
#     print(num)

# class custom_range:
#     def __init__(self, start, end):
#         self.range = range(start, end + 1)
#
#     def __iter__(self):
#         return iter(self.range)
