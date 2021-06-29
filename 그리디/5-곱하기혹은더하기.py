data = list(map(int, input().split()))

print(len(data))
result = int(data[0])
for i in range(1, len(data)):

    i = int(data[i])
    print("i : " , i)
    if i <= 1 or result <= 1 :
        result += i
    else:
        result *= i

print(result)
    