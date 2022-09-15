import random
import math


def shellSort(arr):
    gap = 1
    while (gap < len(arr) / 3):
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = math.floor(gap / 3)
    return arr


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(list)
    print("before: {0}".format(list), end='\n')
    print("after : {0}".format(shellSort(list)), end='\n')