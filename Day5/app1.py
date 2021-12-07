import numpy as np

f = open('input.txt')
x = f.readlines()
f.close()
for i in range(len(x)):
    x[i] = x[i].strip().split(" -> ")
    x[i][0] = x[i][0].strip().split(",")
    x[i][1] = x[i][1].strip().split(",")
    x[i][0][0] = int(x[i][0][0])
    x[i][0][1] = int(x[i][0][1])
    x[i][1][0] = int(x[i][1][0])
    x[i][1][1] = int(x[i][1][1])


class Array:
    def __init__(self, size):
        self.size = size
        self.array = np.zeros((size, size))

    def addPipe(self, input):
        ((x1, y1), (x2, y2)) = input
        if y1 == y2:
            for i in range(x1, x2+1):
                self.array[y2, i] += 1
            for i in range(x2, x1+1):
                self.array[input[1][1], i] += 1
        elif x1 == x2:
            for i in range(y1, y2+1):
                self.array[i, x2] += 1
            for i in range(y2, y1+1):
                self.array[i, x2] += 1

    def sum(self):
        sum = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.array[i, j] > 1:
                    sum += 1
        return sum


p = Array(1000)
for i in x:
    p.addPipe(i)
print(p.sum())
