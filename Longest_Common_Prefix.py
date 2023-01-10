"""
    14. Longest Common Prefix
    - easy
    - LeetCode
"""

"""
    Approach 1

def longestCommonPrefix(strs: list[str]) -> str:
    prefix = ''
    rand_word = strs[0]
    flag = True
    for i in range(1, len(rand_word) + 1):
        for words in strs[1:]:
            if rand_word[:i+1] != words[:i+1]:
                flag = False
        if flag:
            prefix = rand_word[:i+1]
        else:
            break
    return prefix
"""

def longestCommonPrefix(strs: list[str]) -> str:
    rand_word = strs[0]
    prefix = ''
    for i in range(len(rand_word)):
        temp = set(word[:i+1] for word in strs)
        if len(temp) == 1:
            prefix = list(temp)[0]
        else:
            return prefix

strs = list(input().split())
result = longestCommonPrefix(strs)
print(result)