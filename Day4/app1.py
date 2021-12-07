import numpy as np
import sys

f = open('input.txt')
x = f.readlines()
f.close()


class Bingo:
    def __init__(self, input):
        self.array = np.array(input)
        self.guessed = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    def checkWin(self):
        if (max(self.guessed[0]), min(self.guessed[0])) == (1, 1):
            return True
        if (max(self.guessed[1]), min(self.guessed[1])) == (1, 1):
            return True
        if (max(self.guessed[2]), min(self.guessed[2])) == (1, 1):
            return True
        if (max(self.guessed[3]), min(self.guessed[3])) == (1, 1):
            return True
        if (max(self.guessed[4]), min(self.guessed[4])) == (1, 1):
            return True
        if (max(self.guessed[:, 0]), min(self.guessed[:, 0])) == (1, 1):
            return True
        if (max(self.guessed[:, 1]), min(self.guessed[:, 1])) == (1, 1):
            return True
        if (max(self.guessed[:, 2]), min(self.guessed[:, 2])) == (1, 1):
            return True
        if (max(self.guessed[:, 3]), min(self.guessed[:, 3])) == (1, 1):
            return True
        if (max(self.guessed[:, 4]), min(self.guessed[:, 4])) == (1, 1):
            return True
        return False

    def tah(self, cislo):
        x, y = np.where(self.array == cislo)
        if x.size > 0:
            self.guessed[x, y] = 1

    def sumUnmarked(self):
        sum = 0
        for i in range(5):
            for j in range(5):
                if int(self.guessed[i, j]) == 0:
                    sum += int(self.array[i, j])
        return sum


bingos = []
tahy = x[0].split(",")
for i in range(1, len(x)):
    if x[i] == "\n":
        bingos.append(Bingo([x[i+1].strip().replace("  ", " ").split(" "),
                             x[i+2].strip().replace("  ", " ").split(" "),
                             x[i+3].strip().replace("  ", " ").split(" "),
                             x[i+4].strip().replace("  ", " ").split(" "),
                             x[i+5].strip().replace("  ", " ").split(" ")]))
for i in tahy:
    for j in bingos:
        j.tah(i)
        if j.checkWin():
            print(j.sumUnmarked() * int(i))
            sys.exit()
