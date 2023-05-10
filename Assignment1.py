# Number Pattern

n = 5
k = 0
j = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        for j in range(k + 1, k + i):

            print(str(j) + " ", end="")

        j = k + i
        print(j)
        j += 1
        k = j
    else:
        k = k + i - 1
        for j in range(k, k - i + 1, -1):

            print(str(j) + " ", end="")

        j = k - i + 1

        print(j)
