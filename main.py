# silnia/factorial

def factorial_recursive(number: int, result: int) -> int:
    if number <= 1:
        return result

    return factorial_recursive(number - 1, result * number)


def factorial_iteration(number: int) -> int:
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


# fibonacci sequence

"""def fib_recursive(number: int) -> int:
    if number <= 1:
        return number

    return fib_recursive(number - 1)+fib_recursive(number - 2)"""


"""print(factorial_recursive(12, 1))
print(factorial_iteration(5))
print(fib_recursive(8))"""
