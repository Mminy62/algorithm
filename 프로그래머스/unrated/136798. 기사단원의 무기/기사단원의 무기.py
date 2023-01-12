def solution(number, limit, power):
    arms = []

    for n in range(1, number + 1):
        temp = []
        for i in range(1, int(n ** 0.5)+1):
            if n % i == 0:
                temp.append(i)
                temp.append(n//i)
                # if i ** 2 != n:
                #     temp.append(n//i)
        temp = set(temp)
        arms.append(power if len(temp) > limit else len(temp))
    
    return sum(arms)