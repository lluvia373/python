'''
알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.

팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다.

level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.
'''
'''
1번
N = int(input())

for i in range(1, N + 1):
    space_count = N -i
    star_count = i

    for x in range(space_count):
        print(" ", end="")
    for x in range(star_count):
        print("*", end="")
    print()
    
2번    


N = int(input())

for i in range(1, N + 1):
    blank_count = N - i
    star_count = (2 * i) -1

    for x in range(blank_count):
        print(" ", end="")
    for x in range(star_count):
        print("*", end="")
    print()


3번

N = int(input())
for i in range(1, N + 1):
    star_count = N - i + 1
    blank_count = i - 1

    for x in range(blank_count):
        print(" ", end="")
    for x in range(star_count):
        print("*", end="")
    print()
    
4번


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

5번
'''

N = int(input())

for i in range(N):
    for j in range(N):
        if i == j or i + j == N - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
