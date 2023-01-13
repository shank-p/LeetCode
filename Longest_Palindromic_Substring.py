"""
    5. Longest Palindromic Substring
    - easy
    - LeetCode
"""

"""
    Approach 1:

def longestPalindrome(s: str) -> str:
    substrs = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            substrs.append(s[i:j+1])
    
    #print(substrs)
    long_pali = ''
    for i in substrs:
        if len(i) > len(long_pali) and i[::-1] == i:
            long_pali = i
    return long_pali

"""

def longestPalindrome(s: str) -> str:
    pass

s = input()
result = longestPalindrome(s)
print(result)