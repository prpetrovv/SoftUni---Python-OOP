from time import time


def exec_time(func):
    def wrapper(*args):
        starting_time = time()
        func(*args)
        end_time = time()
        return end_time - starting_time

    return wrapper


# Test code
@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10_000_000))
