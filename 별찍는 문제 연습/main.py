# 별찍는 문제 연습용

1
번
N = int(input())

for i in range(1, N + 1):
    space_count = N - i
    star_count = i

    for x in range(space_count):
        print(" ", end="")
    for x in range(star_count):
        print("*", end="")
    print()

2
번

N = int(input())

for i in range(1, N + 1):
    blank_count = N - i
    star_count = (2 * i) - 1

    for x in range(blank_count):
        print(" ", end="")
    for x in range(star_count):
        print("*", end="")
    print()

3
번

N = int(input())
for i in range(1, N + 1):
    star_count = N - i + 1
    blank_count = i - 1

    for x in range(blank_count):
        print(" ", end="")
    for x in range(star_count):
        print("*", end="")
    print()

4
번

N = int(input())
for i in range(1, 2 * N):
    if i <= N:
        blank_count = N - i
        star_count = 2 * i - 1
        for x in range(blank_count):
            print(" ", end="")
        for x in range(star_count):
            print("*", end="")
        print()

    else:
        blank_count = i - N
        star_count = 2 * (2 * N - i) - 1
        for x in range(blank_count):
            print(" ", end="")
        for x in range(star_count):
            print("*", end="")
        print()

5
번


N = int(input())

for i in range(N):
    for j in range(N):
        if i == j or i + j == N - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


6번



N, M = map(int, input().split())

for i in range(N):
    for j in range(M):
        if i == 0:
            print("*", end="")
        if (i > 0) and (i < N - 1):
            if j == 0:
                print("*", end="")
            elif j == M - 1:
                print("*", end="")
            else:
                print(" ", end="")
        if i == N - 1:
            print("*", end="")
    print()

7번


N = int(input())

for i in range(N):
    if i % 2 == 0:
        print("* *")
    else:
        print(" * *")

8번


N = int(input())

for i in range(N):
    space = " " * (N - i - 1)
    if i == 0:
        print(space + "*")
    else:
        print(space + "*" + " " * (2 * i -1) + "*")

for i in range(N + 1, 2 * N):
    space = " " * (i - N)
    if i == 2 * N - 1:
        print(space + "*")
    else:
        print(space + "*" + " " * (i - N) + "*")



