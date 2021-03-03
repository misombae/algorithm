#한번 계산된 결과 캐싱하기 위한 리스트 초기화
d = [0] * 100

#피보나치 함수 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    if x ==1 or x==2 :
        return 1
    if d[x] != 0 : #계산한적 있는 문제라면 계산되었던 값 반환
        return d[x]
    
    d[x]= fibo(x-1) + fibo(x-2) #계산하지 않은 문제는 결과 반환
    return d[x]

print(fibo(99))