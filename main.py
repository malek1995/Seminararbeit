# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def perm(start, end=[]):

    if(len(start) == 0):
        print(end)
        print("here is the result : ", quickselect(end, 4))
        global n
        n += 1
    else:
        for i in range(len(start)):
            perm(start[:i] + start[i+1:], end + start[i:i+1])

def partition(list, index):
    list[-1], list[index] = list[index], list[-1]
    pivot = list[-1]
    i = 0
    for j in range(len(list)-1):
        if list[j] <= pivot:
            list[i], list[j] = list[j], list[i]
            i += 1
    list[i], list[-1] = list[-1], list[i]
    return i

def quickselect(list, index):
    if len(list) == 1:
        return list[0]
    pivot = random.randint(0, len(list) - 1)
    indexOfPivot = partition(list, pivot)
    indexNew = indexOfPivot + 1
    if indexNew == index:
        return list[indexOfPivot]
    if index < indexNew:
        return quickselect(list[:indexOfPivot], index)
    else:
        return quickselect(list[indexOfPivot+1:], index-indexNew)

def medianOfFive(list):
    if list[0] > list[1]:
        list[0], list[1] = list[1], list[0]
    if list[2] > list[3]:
        list[2], list[3] = list[3], list[2]
    if list[2] < list[0]:
        list[1], list[3] = list[3], list[1]
        list[2] = list[0]
    list[0] = list[4]
    if list[0] > list[1]:
        list[0], list[1] = list[1], list[0]
    if list[0] < list[2]:
        list[1], list[3] = list[3], list[1]
        list[0] = list[2]
    if list[0] < list[3]:
        list[0], list[2] = list[2], list[0]
    else:
        list[2], list[3] = list[3], list[2]
    return list

if __name__ == '__main__':
    n = 0
    perm([1, 2, 3, 4, 5, 6, 7])
    print(n)
    #perm([10, 20, 30, 40, 50])


