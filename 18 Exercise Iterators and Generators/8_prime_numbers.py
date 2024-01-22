from math import sqrt


def get_primes(numbers: list):
    for number in numbers:
        if number > 1:
            for i in range(2, int(sqrt(number)) + 1):
                if number % i == 0:
                    break
            else:
                yield number


# Test Code
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
