def possible_permutations(given_list: list):
    if len(given_list) <= 1:
        yield given_list
    else:
        for i in range(len(given_list)):
            for perm in possible_permutations(given_list[:i] + given_list[i + 1:]):
                yield [given_list[i]] + perm


# Test Code
[print(n) for n in possible_permutations([1, 2, 3])]
