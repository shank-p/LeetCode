"""
    13. Roman to Integer
    - Easy
    - LeetCode
"""

def romanToInt(s: str) -> int:
    roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    sum = 0
    
    for i in range(len(s)-1):
        if roman_numerals[s[i]] < roman_numerals[s[i+1]]:
            sum -= roman_numerals[s[i]]
            continue
        sum += roman_numerals[s[i]]
    sum += roman_numerals[s[-1]]
    return sum

s = input()
result = romanToInt(s)
print(result)