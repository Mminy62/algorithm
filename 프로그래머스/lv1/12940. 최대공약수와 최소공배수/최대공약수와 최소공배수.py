# def gcd(a, b): #a 가 더 큰 수로 가정
#     if a < b: b, a = a, b
#     if b == 0: 
#         return a
#     else:
#         return gcd(b, a % b)
    
# def lcm(m, g):
#     return m // g
import math

def solution(n, m):
    g = math.gcd(n, m)
    l = n*m//g
    
    return [g, l]