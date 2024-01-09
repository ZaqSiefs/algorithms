def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

def verify(index):
    if index != None:
        print("Item is at index: ", index)
    else:
        print("Item is not in list")

list = [1,2,3,4,5,6,7,8,9,10,11,12]

answer = binary_search(list, 13)

verify(answer)
