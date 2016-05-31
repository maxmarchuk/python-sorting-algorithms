#!/usr/bin/python

def merge_sort(lst):
    if len(lst) > 1:
        # get the middle of the list
        middle = len(lst) // 2

        # split the list in half
        leftHalf = lst[:middle]
        rightHalf = lst[middle:]

        # sort both halves
        merge_sort(leftHalf)
        merge_sort(rightHalf)

        i = 0 # left half counter
        j = 0 # right half counter
        k = 0 # result array counter


        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                lst[k] = leftHalf[i]
                i += 1
            else:
                lst[k] = rightHalf[j]
                j += 1
            k += 1

        # take care of any remaining elements for the left half
        while i < len(leftHalf):
            lst[k] = leftHalf[i]
            k += 1
            i += 1

        # take care of any remaining elements for the right half
        while j < len(rightHalf):
            lst[k] = rightHalf[j]
            j += 1
            k += 1

if __name__ == "__main__":
    import sys
    aList = []
    for i in range(1, len(sys.argv)):
        try:
            aList.append(int(sys.argv[i]))
        except Exception:
            print("Detected non-integer value in parameters. '{}'".format(sys.argv[i]))
    merge_sort(aList)
    print("sorted: ", aList)


