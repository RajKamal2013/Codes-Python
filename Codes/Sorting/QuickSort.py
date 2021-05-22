def partition(arr, start, end):
    pivot = arr[end]
    i = start;
    j = i - 1

    while (i < end):
        if (arr[i] < pivot):
            j = j + 1
            arr[i], arr[j] = arr[j], arr[i]

        i = i + 1

    j = j + 1
    arr[j], arr[end] = arr[end], arr[j]
    return j


def quickSort(arr, start, end):
    if (start < end):
        pivot = partition(arr, start, end)
        quickSort(arr, start, pivot - 1)
        quickSort(arr, pivot + 1, end)

def qsort(arr):
    quickSort(arr, 0, len(arr) - 1)


