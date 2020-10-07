# 최대공약수 계산( 유클리드 호제법 )
# 유클리드 호제법 
# : A, B에 대해 ( A > B ) A를 B로 나눈 나머지를 R
# A와 B의 최대공약수는 B와 R의 최대공약수와 같다.

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)