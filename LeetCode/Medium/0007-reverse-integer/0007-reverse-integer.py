class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            sx = "-" + str(x)[1:][::-1]
            print(sx)
        else:
            sx = str(x)[::-1]
        
        sx = int(sx)
        if sx < -2**31 or sx > 2**31-1:
            sx = 0
        return sx