#부품찾기 계수정렬

n = int(input())
array = [0] * 1000000

for i in input().split():
    array[int(i)] = 1 

m = int(input())
array_search = list(map(int, input().split()))
for i in array_search:
    if array[i] == 1:
        print('Yes', end = ' ')
    else : 
        print('No', end = ' ')