f = open('input.txt')
x = f.readline()
f.close()

x2 = x.split(",")
x1 = [int(numeric_string) for numeric_string in x2]
dict = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
for i in x2:
    if i == "0":
        dict["0"] += 1
    elif i == "1":
        dict["1"] += 1
    elif i == "2":
        dict["2"] += 1
    elif i == "3":
        dict["3"] += 1
    elif i == "4":
        dict["4"] += 1
    elif i == "5":
        dict["5"] += 1
    elif i == "6":
        dict["6"] += 1
    elif i == "7":
        dict["7"] += 1
    elif i == "8":
        dict["8"] += 1
for i in range(256):
    dict["0"], dict["1"], dict["2"], dict["3"], dict["4"], dict["5"], dict["6"], dict["7"], dict["8"] = dict["1"], dict["2"], dict["3"], dict["4"], dict["5"], dict["6"], dict["0"] + dict["7"], dict["8"], dict["0"]
print(dict["0"] + dict["1"] + dict["2"] + dict["3"] + dict["4"] + dict["5"] + dict["6"] + dict["7"] + dict["8"])
