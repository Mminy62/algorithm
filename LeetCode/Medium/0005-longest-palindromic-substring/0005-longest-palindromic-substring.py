class Solution:
    def longestPalindrome(self, s: str) -> str:
#         result = ''
#         for l in range(len(s)):
#             for r in range(l+1, len(s)+1):
#                 if s[l:r] == s[l:r][::-1] and len(result) < r-l:
#                     result = s[l:r]

#         return result
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        longest = ""
        for i in range(len(s)):
            odd_palindrome = expand_around_center(i, i)
            even_palindrome = expand_around_center(i, i + 1)
            
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
                
        return longest