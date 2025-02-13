'''answer = ""
array = [input().strip() for _ in range(5)]
max_len = max(len(row) for row in array)

for col in range(max_len):
    for row in range(len(array)):
        if col < len(array[row]):
            answer += array[col][row]

print(answer)'''

[print("asd") for _ in range(5)]