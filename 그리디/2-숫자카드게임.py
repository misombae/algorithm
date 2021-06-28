# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다. 
# 1. 숫자가 쓰인 카드가 N(행)*M(열)형태로 놓여있다. 
# 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다. 
# 3. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑는다.. 
# 4. 따라서 처음에 카드를 골라 낼 행을 선택할 때, 
# 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세운다.

n, m = map(int, input().split())

result = 0
for line in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

