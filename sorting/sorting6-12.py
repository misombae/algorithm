#두 배열의 원소 교체
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]: #b가 큰 경우 교체
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
