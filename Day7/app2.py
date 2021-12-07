f = open('input.txt')
x = f.readline()
f.close()
x = x.split(",")
x = [int(z) for z in x]
sol = []
for i in range(max(x)):
    t = 0
    for j in x:
        n = abs(j-i)
        t += (n*(n+1))/2
    sol.append(t)
print(min(sol))
