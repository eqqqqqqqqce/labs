# TODO решите задачу

def task() -> float:
    arr = 0
    s = 0
    z1 = 0
    z2 = 0
    f = open("input.json", "r")
    arr = f.readlines()

    for i in range(len(arr)):
        if arr[i].find("score") != -1:
            z1 = float(arr[i][((arr[i].find("score")) + 8):len(arr[i]) - 2])

        elif (arr[i].find("weight")) != -1:
            z2 = float(arr[i][((arr[i].find("weight")) + 9):len(arr[i]) - 1])

        if(z1 != 0) and (z2 != 0):
            s += z1 * z2
            z1, z2 = 0, 0

    f.close()
    return round(s, 3)

print(task())

