# Zigzag pattern

def zigzag(arr):
    l = len(arr)
    cntr = int(l/2)
    arrGreater = []
    arrLowers = []
    newArr = []

    for i in range(0, cntr):
        arrLowers.append(arr[i])

    for i in range(l-1, cntr-1, -1):
        arrGreater.append(arr[i])

    for i in range(0, cntr):
        newArr.append(arrGreater[i])
        newArr.append(arrLowers[i])

    if (l % 2 != 0):
        newArr.append(arrGreater[len(arrGreater)-1])
    return newArr


arr = [1, 2, 3, 4, 5]
ans = zigzag(arr)
print(ans)
