import sys
input = sys.stdin.readline

n = int(input())
moneys = []
for _ in range(n):
    moneys.append(int(input()))

moneys.sort(reverse=True)

result = 0
for i in range(n):
    money = moneys[i] - i
    if money > 0:
        result += money

print(result)