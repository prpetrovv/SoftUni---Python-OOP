def fibonacci():
    curr_number, next_number = 0, 1
    while True:
        yield curr_number
        curr_number, next_number = next_number, curr_number + next_number


# Test Code
generator = fibonacci()
for i in range(5):
    print(next(generator))
