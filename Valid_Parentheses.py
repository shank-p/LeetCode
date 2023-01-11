"""
    20. Valid Parentheses
    - easy
    - LeetCode
"""

def isValid(s: str) -> bool:
    parantheses = {'(':')', '[':']', '{':'}'}
    stack = []
    
    for i in s:
        if i in parantheses.keys():
            stack.append(parantheses[i])
        elif stack and stack[-1] == i:
            stack.pop()
        else:
            return False

    return stack == []

s = input()
result = isValid(s)
print(result)