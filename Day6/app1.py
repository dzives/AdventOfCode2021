f = open('input.txt')
x = f.readline()
f.close()

x2 = x.split(",")
x1 = [int(numeric_string) for numeric_string in x2]
for i in range(256):
    count = 0
    for j in range(len(x1)):
        if x1[j] == 0:
            x1[j] = 6
            count += 1
        else:
            x1[j] += -1
    for i in range(count):
        x1.append(8)
print(len(x1))
