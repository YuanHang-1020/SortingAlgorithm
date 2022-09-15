import random


def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(list)
    print("before: {0}".format(list), end='\n')
    print("after : {0}".format(bubbleSort(list)), end='\n')
