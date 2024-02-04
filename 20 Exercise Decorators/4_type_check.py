def type_check(param_type):
    def decorator(func):
        def wrapper(parameter):
            if not isinstance(parameter, param_type):
                return "Bad Type"
            return func(parameter)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))
