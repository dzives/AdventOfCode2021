f = open("input.txt")
x = f.readlines()
f.close()
count = 0
for i in range(0, len(x)):
    if int(x[i]) + int(x[i-1]) + int(x[i-2]) > int(x[i-1]) + int(x[i-2]) + int(x[i-3]):
        count += 1
print(count)
