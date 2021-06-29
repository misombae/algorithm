# 공포도가 X인 모험가는 반드시 X명 이상으로 구성해야 모험가 그룹에 참가할 수 있습니다. 
# N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하시오 
# 몇 명의 모험가는 마을에 그대로 남아 있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없습니다.

data = list(map(int, input().split()))

result = 0
count = 0
for x in data:
    count +=1
    if count>= x:
        result +=1
        count = 0


print(result)