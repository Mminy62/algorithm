N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

for i in sorted(numbers):
    print(i)