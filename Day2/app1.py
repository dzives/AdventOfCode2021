f = open('input.txt')
x = f.readlines()
f.close()
h = 0
d = 0
for i in x:
    y = i.split(" ")
    if y[0] == "forward":
        h += int(y[1])
    elif y[0] == "up":
        d -= int(y[1])
    elif y[0] == "down":
        d += int(y[1])

print(d*h)
