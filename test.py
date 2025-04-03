#Basic sorting algorithm

def bubble_sort(arr: []) -> []:
    for i in range(len(arr)):
        checker = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                checker = True
        if not checker:
            return arr

    return arr

def selection_sort(arr: []) -> []:
    for i in range(len(arr)):
        min_element = i
        for j in range(i,len(arr)):
            if arr[min_element] > arr[j]:
                min_element = j
        arr[min_element], arr[i] = arr[i], arr[min_element]

    return arr

print(bubble_sort([3, 2, 6, -111, 1, 1]))
print(selection_sort([3,3,3,3,1,-444,123]))


###boho pants are the best
