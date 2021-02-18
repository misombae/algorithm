#떡볶이 떡 만들기
n, m = list(map(int, input().split())) #n: 떡의 개수, m : 요청한 떡의 길이 
array = list(map(int, input().split())) #떡의 개별 높이 


#출력조건 : 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

#이진 탐색 
#절단기에 설정할수 있는 높이의 최댓값 
def binary_search(array, target, start, end):
    result = 0 
    while (start <= end ):
        total = 0
        mid = (start+end)//2
        for x in array: 
            if x > mid : #잘린 경우 요청한 떡의 길이 더함 
                total += x - mid
        
            if total < m : # 요청한 길이보다 적을 경우 절단기의 길이를 줄임 
                end = mid - 1
            else : # 떡의 양이 충분한 경우  
                result =  mid 
                start = mid + 1 
    return result 


result = binary_search(array, m, 0, max(array))
print(result)

