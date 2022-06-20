def star(n):
    if n == 3:
        star_list = ["***", "* *", "***"]
        return star_list
    else:
        new_star = [x * 3 for x in star(n//3)] + [x + ' '*(n//3) + x for x in star(n//3)] + [x * 3 for x in star(n//3)] #['*','*','*'] 이렇게 연결지어짐
        return new_star

for i in star(int(input()):
    print(i)
