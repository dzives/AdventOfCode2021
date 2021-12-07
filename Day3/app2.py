f = open('input.txt')
x = f.readlines()
f.close()
gamma = ""
epsilon = ""
x1 = x.copy()
x2 = x.copy()


def mostLeastCommonBit(x: str):
    one = 0
    zero = 0
    for i in x:
        if i == "0":
            zero += 1
        elif i == "1":
            one += 1
    if one == zero:
        return ("0", "0", True)
    elif one > zero:
        return ("1", "0", False)
    elif one < zero:
        return ("0", "1", False)


def getColumn(arr, c):
    str = ""
    for i in arr:
        str = str + i[c]
    return str


a = len(x[0]) - 2
c1 = 0
while len(x1) != 1:
    z, y, e = mostLeastCommonBit(getColumn(x1, c1))
    if c1 == a or len(x1) == 2 or e == True:
        z = "1"
    if z == "1":
        for i in range(len(x1)):
            if x1[i][c1] == "0":
                x1[i] = None
    if z == "0":
        for i in range(len(x1)):
            if x1[i][c1] == "1":
                x1[i] = None
    x1 = list(filter(None, x1))
    c1 += 1
c2 = 0
while len(x2) != 1:
    y, z, e = mostLeastCommonBit(getColumn(x2, c2))
    if c2 == a or len(x2) == 2 or e == True:
        print("ahoj2")
        z = "0"
    if z == "1":
        for i in range(len(x2)):
            if x2[i][c2] == "0":
                x2[i] = None
    if z == "0":
        for i in range(len(x2)):
            if x2[i][c2] == "1":
                x2[i] = None
    x2 = list(filter(None, x2))
    c2 += 1

print(int(x1[0], 2)*int(x2[0], 2))
