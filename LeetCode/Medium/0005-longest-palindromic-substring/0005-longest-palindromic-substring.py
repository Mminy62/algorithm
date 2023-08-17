class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 가장 긴 팰린드롬 문자열
        result = ''
        for l in range(len(s)):
            for r in range(l+1, len(s)+1):
                if s[l:r] == s[l:r][::-1] and len(result) < r-l:
                    result = s[l:r]
        if not result and len(s) == 1:
            result = s
        return result
        