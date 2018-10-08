# python3
import sys


def mergeSort(alist):
    count = 0
    leftcount = 0
    rightcount = 0
    blist = []
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        leftcount, lefthalf = mergeSort(lefthalf)
        rightcount, righthalf = mergeSort(righthalf)

        i = 0
        j = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                blist.append(lefthalf[i])
                i += 1
            else:
                blist.append(righthalf[j])
                j += 1
                count += len(lefthalf[i:])

        while i < len(lefthalf):
            blist.append(lefthalf[i])
            i += 1

        while j < len(righthalf):
            blist.append(righthalf[j])
            j += 1
    else:
        blist = alist[:]

    return count + leftcount + rightcount, blist


if __name__ == "__main__":
    i = 0
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:]
    i, list= mergeSort(a)
    print(i)