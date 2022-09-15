import random


def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    return arr


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(list)
    print("before: {0}".format(list), end='\n')
    print("after : {0}".format(insertionSort(list)), end='\n')
