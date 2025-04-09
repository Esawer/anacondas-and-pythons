# Basic sorting algorithm

"""def bubble_sort(arr: []) -> []:
    for i in range(len(arr)):
        checker = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                checker = True
        if not checker:
            return arr

    return arr"""




"""def selection_sort(arr: []) -> []:
    for i in range(len(arr)):
        min_element = i
        for j in range(i, len(arr)):
            if arr[min_element] > arr[j]:
                min_element = j
        arr[min_element], arr[i] = arr[i], arr[min_element]

    return arr

def merge_sort(arr: []) -> []:
    if len(arr) <= 1:
        return arr
    
    left_half = [arr[:len(arr)//2]]
    right_half = [arr[len(arr)//2:]]
    return merge(left, right)

def merge(left,right):
    """

#deep seek helped me out a little, it is important to add: if not arr: return -1; eventually return "not found" and also add return function() - as it is a reculusive function and needs return in every case,

"""def binary_search(arr: [], needle):
    if not arr:
        return -1

    middle = (len(arr)) // 2
    if needle == arr[middle]:
        return f"found it - {arr[middle]}"


    if needle > arr[middle]:
        return binary_search(arr[middle+1:], needle)
    else:
        return binary_search(arr[:middle],needle)"""





"""print(bubble_sort([3, 2, 6, -111, 1, 1]))
print(selection_sort([3, 3, 3, 3, 1, -444, 123]))
print(binary_search([1,2,3,4,5,6,7,8,9,19],19))


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

def fib_recursive(number: int) -> int:
    if number <= 1:
        return number

    return fib_recursive(number - 1)+fib_recursive(number - 2)


print(factorial_recursive(12, 1))
print(factorial_iteration(5))
print(fib_recursive(8))


"""
