n, k = map(int, input().split())

result = 0

while True : 
    target = n % k 
    n = n - target
    result += target

    if n < k : 
        break 

    n = n // k 
    result += 1

result += n-1 #남은수가 5인경우 1이 되기 위해선 -1을 4번 빼줘야함 (5-1번)
print(result)

print(result)



