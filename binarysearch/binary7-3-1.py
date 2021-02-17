from bisect import bisect_left, bisect_right

#값이 특정 범위에 속하는 데이터 개수 구하기 
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
#값이 4인 데이터 개수 출력
result = count_by_range(a, 4, 4)
print(result)
#값이 -1, 3 범위에 있는 데이터 개수 출력 
result = count_by_range(a, -1, 3)
print(result)

def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index


