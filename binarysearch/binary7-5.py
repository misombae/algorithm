#부품찾기 

def binary_search(array, target, start, end):
    while start <= end : 
        mid = (start+end) // 2 
        if array[mid] > target: #찾는 값이 중간 값 보다 작은 경우  
            end = end - 1
        elif array[mid] < target: #찾는 값이 중간 값 보다 큰 경우
            start = start +1  
        else: 
            return 'YES'  
    return 'NO'

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
search_array = list(map(int, input().split()))

for i in search_array: 
    result = binary_search(array, i, 0, n-1)
    if result == 'NO':
        print('NO', end = ' ')
    else:
        print('YES', end = ' ')
            

    