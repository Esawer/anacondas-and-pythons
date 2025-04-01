#Basic sorting algorithm

def abc(arr: []) -> []:
    for i in range(len(arr)):
        checker = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                checker = True
        if not checker:
            return arr

    return arr

print(abc([3,2,6,-111,1,1]))
print(abc([2,1,1]))



