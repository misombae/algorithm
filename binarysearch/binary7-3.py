
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] < target:
            end = mid - 1
        elif array[mid] > target:
            start = mid + 1
        else:
            return mid
    return None 


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("존재하지않음")
else:
    print(result+1)
