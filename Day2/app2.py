f = open('input.txt')
x = f.readlines()
f.close()
h = 0
d = 0
a = 0
for i in x:
    y = i.split(" ")
    if y[0] == "forward":
        h += int(y[1])
        d += a * int(y[1])
    elif y[0] == "up":
        a -= int(y[1])
    elif y[0] == "down":
        a += int(y[1])

print(h*d)
