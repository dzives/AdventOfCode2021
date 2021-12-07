f = open('input.txt')
x = f.readlines()
f.close()
gamma = ""
epsilon = ""


def mostLeastCommonBit(x: str) -> (str):
    one = 0
    zero = 0
    for i in x:
        if i == "0":
            zero += 1
        elif i == "1":
            one += 1
    return ("1", "0") if one > zero else ("0", "1")


def getColumn(arr, c):
    str = ""
    for i in arr:
        str = str + i[c]
    return str


for i in range(len(str(x[0])) - 1):
    g, e = mostLeastCommonBit(getColumn(x, i))
    gamma = gamma + g
    epsilon = epsilon + e

print(int(gamma, 2)*int(epsilon, 2))
