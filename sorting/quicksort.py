array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start>=end: #원소가 한개인 경우 종료
        return
    pivot = start #피벗값 설정:첫번째원소
    left = start+1
    right = end
    while left<=right: #left가 right보다 크면 ? 엇갈린 경우이기 때문에 분할이루어져서 while문 종료
        while left <= end and array[left] <= array[pivot]: #왼쪽부터 피벗보다 큰값 찾을때까지 +1
            left +=1
        while right > start and array[right] >= array[pivot]:  #오른쪽부터 피벗보다 작은 값 찾을때까지 -1
            right -=1
        if left > right: #엇갈렷다면 교체 피벗과 값 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: #엇갈리지 않았다면
            array[right], array[left] = array[left], array[right]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)