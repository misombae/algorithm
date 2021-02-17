#부품찾기 집합 자료형 
#단순히 특정한 데이터가 존재하는지 검사할때 효과적
n = int(input())
array = set(map(int, input().split()))

m = int(input())
array_search = list(map(int, input().split()))
for i in array_search:
    for i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
    