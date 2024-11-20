n, m = input("").split()
arr_total = []
arr_print = []
for i in range(int(n)):
    arr_total.append(0)
for i in range(int(m)):
    arr_print.append(0)
def per(zero):
    if zero == int(m):
        for i in range(int(m)):
            print(arr_print[i], end = " ")
        print()
        return

    for i in range(int(n)):
        if arr_total[i] == 0:
            arr_print[zero] = i + 1
            arr_total[i] = 1
            per(zero + 1)
            arr_total[i] = 0
per(0)
