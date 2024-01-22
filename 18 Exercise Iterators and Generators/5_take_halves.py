def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for _ in range(n):
            result.append(next(seq))
        return result
        # Can be done with compression
        # return [next(seq) for _ in range(n)]

    return take, halves, integers


# Test Code
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
