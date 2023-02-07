import sys
import heapq

n = int(sys.stdin.readline())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))

def calculate(cards):
    result = 0

    while len(cards) != 1:
        one = heapq.heappop(cards)
        two = heapq.heappop(cards)
        sum_value = one + two
        result += sum_value
        heapq.heappush(cards, sum_value)

    return result

print(calculate(cards))