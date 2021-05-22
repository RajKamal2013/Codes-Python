import random

class IntFileGenerator:
    """   -> Multiple Constructor not supported, we need to learn Decorator
    def __init__(self):
        self.size = 30
        self.range = 500
        self.inputFileName = "input.txt"
        self.outputFileName = "output.txt"
     """
    def __init__(self, size, range=50):
        self.size = size
        self.range = range
        self.inputFileName = "input.txt"
        self.outputFileName = "output.txt"

    def read(self):
        print("Collecting Data from File:", self.inputFileName, "in array")
        file = open(self.inputFileName, "r")
        arr = list()

        for line in file:
            arr.append(int(line))

        return arr

    def generate(self):
        print("Generating:", self.size, "Random Numbers in File:", self.inputFileName)
        file= open(self.inputFileName, "w")
        file.write(str(self.size))
        file.write("\n")
        for i in range(self.size):
            data1 = random.randint(0, self.range)
            file.write(str(data1))
            file.write("\n")

        file.flush()
        file.close()

    def write(self, arr):
        print("Copying data to File:", self.outputFileName)
        file = open(self.outputFileName, "w")

        arrlen = len(arr)
        file.write(str(arrlen))
        file.write("\n")

        for num in arr:
            file.write(str(num))
            file.write("\n")

        file.close()








