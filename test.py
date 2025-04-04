#Basic sorting algorithm

def bubble_sort(arr: []) -> []:
    for i in range(len(arr)):
        checker = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                checker = True
        if not checker:
            return arr

    return arr




def selection_sort(arr: []) -> []:
    for i in range(len(arr)):
        min_element = i
        for j in range(i, len(arr)):
            if arr[min_element] > arr[j]:
                min_element = j
        arr[min_element], arr[i] = arr[i], arr[min_element]

    return arr

#deep seek helped me out a little, it is important to add: if not arr: return -1; eventually return "not found" and also add return function() - as it is a reculusive function and needs return in every case,
# or smth like that

#all else was quite good few changes here and there, but mostly good.
#ok ok ok
def binary_search(arr: [], needle):
    if not arr:
        return -1

    middle = (len(arr)) // 2
    if needle == arr[middle]:
        return f"found it - {arr[middle]}"


    if needle > arr[middle]:
        return binary_search(arr[middle+1:], needle)
    else:
        return binary_search(arr[:middle],needle)



"""print(bubble_sort([3, 2, 6, -111, 1, 1]))
print(selection_sort([3, 3, 3, 3, 1, -444, 123]))"""
print(binary_search([1,2,3,4,5,6,7,8,9,19],19))


<<<<<<< HEAD
=======
###boho pants are the best
#ooo
>>>>>>> 242d8cd66c9310e370723b171c797ead4844d736
