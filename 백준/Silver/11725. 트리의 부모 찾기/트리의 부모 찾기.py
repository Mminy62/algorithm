import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
# 그래프 순회처럼 풀기
Tree = [[] for _ in range(N + 1)] # 이진트리라고 명시하지 않음. #자식노드의 수가 2이상이 될 수 있음
parent = [0] * (N + 1)

for _ in range(N-1):
    x, y = map(int, input().split())
    Tree[x].append(y)
    Tree[y].append(x)

# 다 입력 -> 그래프 순회 같음
# 부모 찾아주기
def find_parent(root):
    for i in Tree[root]:
        if parent[i] == 0:
            parent[i] = root
            find_parent(i)

find_parent(1)
for i in range(2, N + 1):
    print(parent[i])