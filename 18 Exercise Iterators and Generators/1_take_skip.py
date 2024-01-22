class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.count:
            raise StopIteration()
        result = self.current * self.step
        self.current += 1
        return result


# Test Code
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
