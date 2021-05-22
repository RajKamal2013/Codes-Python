import time

from Codes.Sorting.QuickSort import qsort
from Codes.Util import FileGenerator
from Codes.Sorting import QuickSort

def main():
    f = FileGenerator.IntFileGenerator(1000)
    f.generate()
    arr = range(1, 50, 3)
    f.write(arr)
    arr = f.read()
    count = arr[0]
    arr = arr[1:]
    print("Array Generated:", arr)
    start = time.time_ns()
    qsort(arr)
    end = time.time_ns()
    print("Time Spent in Sorting via QSort(in nanosec):", (end-start))
    f.write(arr)
    print("Array Sorted:", arr)


main()

if __name__ == '___main__;':
    print("Running Main")