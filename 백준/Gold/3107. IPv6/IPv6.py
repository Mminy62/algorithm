ip_list = input().split(':')

# 숫자가 있으면 4자리로 맞추 0 넣고, : 추가, count
cnt = 0
for i in range(len(ip_list)):
    if ip_list[i]:
        ip_list[i] = ip_list[i].zfill(4) + ':'
        cnt += 1


if cnt < 8:
    # 생략이 2개인지 1개인지 구별
    if ip_list.count('') == 2:
        del ip_list[ip_list.index('')]

    ip_list[ip_list.index('')] = '0000:' * (8-cnt)
ip_list[-1] = ip_list[-1][:-1]
print(''.join(ip_list))
