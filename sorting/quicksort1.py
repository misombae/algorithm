#아래 퀵 정렬 소스코드는 전통 퀵 정렬의 분할 방식과는 조금 다른데,
#피벗과 데이터를 비교하는 비교 연산 횟수가 증가하므로 시간면에서는 조금 비효율적이다. 하지만 더 직관적이고 기억하기 쉽다는 장점이 있다.

array = [7,5,9,0,3,1,6,2,4,8]
def quick_sort(array):
    if len(array)<=1: return array #리스트가 하나 이하의 원소만을 담고 있다면 종료
    pivot = array[0] #피벗 설정
    tail = array[1:] #피벗을 제외한 리스트
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분 #피벗보다 값이 작은 데이터만 골라서 left_side에 넣음
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분 #피벗보다 값이 큰 데이터만 골라서 right_side에 넣음

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스르르 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side) #왼쪽리스트+피벗값+오른쪽리스트 를 리턴
print(quick_sort(array))