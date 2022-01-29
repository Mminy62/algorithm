import sys

sen = sys.stdin.readline().rstrip()


croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for k in croatia:
    sen = sen.replace(k,"1")

print(len(sen))
