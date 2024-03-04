n, m = map(int, input().split())
book = {}
book_list = []
result = []
for i in range(n):
    name = input()
    book[name] = i + 1
    book_list.append(name)

for _ in range(m):
    problem = input()
    if problem.isdigit():
        index = int(problem)
        result.append(book_list[index - 1])
    else:
        result.append(book[problem])

for _ in range(len(result)):
    print(result[_])