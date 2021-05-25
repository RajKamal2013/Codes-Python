import time

from Codes.Sorting.HeapSort import hSort
from Codes.Sorting.MergeSort import msort
from Codes.Sorting.QuickSort import qsort
from Codes.Util import FileGenerator
from Codes.Sorting import QuickSort

def display(arr, str):
    banner = "--------------------"
    print(banner, str, banner)
    print(arr)


def main():

    # ----------------------------- QuickSort -------------------------
    Qf = FileGenerator.IntFileGenerator(1000, 600, "QsortInput.txt", "QsortOutput.txt")
    Qf.generate()
    Qarr = range(1, 50, 3)
    Qf.write(Qarr)
    Qarr = Qf.read()
    count = Qarr[0]
    Qarr = Qarr[1:]
    display(Qarr, "QuickSort: Input Array")
    start = time.time_ns()
    qsort(Qarr)
    end = time.time_ns()
    print("Time Spent in Sorting via QSort(in nanosec):", (end-start))
    Qf.write(Qarr)
    display(Qarr, "QuickSort: Output Array")

    # ----------------------------- MergeSort ------------------------
    Mf = FileGenerator.IntFileGenerator(1000, 600, "MsortInput.txt", "MsortOutput.txt")
    Mf.generate()
    Marr = Mf.read()
    Marr = Marr[1:]
    display(Marr, "MergeSort: Input Array")
    start = time.time_ns()
    msort(Marr)
    end = time.time_ns()
    print("Time Spent in Sorting via MSort(in nanosec):", (end - start))
    display(Marr, "MergeSort:Output Array")
    Mf.write(Marr)

    # ----------------------------- Heap Sort ------------------------
    Hf = FileGenerator.IntFileGenerator(1000, 600, "HsortInput.txt", "HsortOutput.txt")
    Hf.generate()
    Harr = Hf.read()
    Harr = Harr[1:]
    display(Harr, "HeapSort: Input Array")
    start = time.time_ns()
    hSort(Harr)
    end = time.time_ns()
    print("Time Spent in Sorting via HSort(in nanosec):", (end - start))
    display(Harr, "HeapSort:Output Array")
    Mf.write(Harr)





main()

if __name__ == '___main__;':
    print("Running Main")