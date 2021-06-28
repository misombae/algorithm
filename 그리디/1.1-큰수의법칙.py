#n = 5
#m = 8 
#k = 3
#data = [2, 4, 5, 6, 4]

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

k_count = int(m/(k+1))*k
k_count = k_count + int(m%(k+1))
print(k_count)

result = 0 
result = k_count * data[n-1] #가장 큰 수 횟수 * 가장 큰 수
print(result)
result += (m-k_count) * data[n-2] #나머지 횟수 * 두번째 큰 수 

print(result)
