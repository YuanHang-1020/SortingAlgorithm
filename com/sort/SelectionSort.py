import random


def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(list)
    print("before: {0}".format(list), end='\n')
    print("after : {0}".format(selectionSort(list)), end='\n')
