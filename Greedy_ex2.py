# [ 곱하기 혹은 더하기 ] 
# 숫자로만 이루어진 문자열이 주어졌을 때, 
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자 사이에 x 혹은 + 를 넣어 
# 결과적으로 만들어질 수 있는 가장 큰 수를 구하라. 

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1 :
        result += num
    else :
        result *= num
    
print(result)