"""
    9. Palindrome Number
    - Easy
    - LeetCode
"""

"""
    Approach 1:

def isPalindrome(x: int) -> bool:
    s = str(x)
    return s==s[::-1]

"""

# runtime half of n worst case.
def isPalindrome(x: int) -> bool:
    s = str(x)
    for i in range(len(s)//2):
        print(s[i], s[-i-1])
        if s[i] != s[-i-1]:
            return False
    return True


x = int(input())
result = isPalindrome(x)
print(result)