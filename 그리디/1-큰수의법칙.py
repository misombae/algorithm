# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다. 
# 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 k번을 초과하여 더해질 수 없는 것이 특징이다.
# 예를 들어 2,4,5,4,6, M=8, K=3인 경우 큰 수의 법칙에 따라 6+6+6+5+6+6+6+5=46

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
print(data)

data.sort()
first_big = data[n-1]
second_big = data[n-2]

result = 0
count = 0

while True:
    for i in range(k):
        if count == m:
            break
        result += first_big
        count += 1
        print(first_big)
    if count == m:
        break
    result += second_big
    count += 1
    print(second_big)

print(result)
    
    
    