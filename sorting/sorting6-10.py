#위에서 아래로
#n = int(input())

#array = []
#for i in range(n):
#    array.append(int(input())) #n개 입력받아서 array에 저장

array = list(map(int, input().split()))
array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')