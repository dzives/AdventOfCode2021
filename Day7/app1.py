f = open('input.txt')
x = f.readline()
f.close()
x = x.split(",")
x = [int(z) for z in x]
sol = []
for i in range(max(x)):
    t = 0
    for j in x:
        t += abs(i-j)
    sol.append(t)
print(min(sol))
