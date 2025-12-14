# ## Strings — Additional Core Problems

# ### 1. Longest Common Prefix
# Given a list of strings, find the longest starting substring (prefix) that all strings share.
# Example idea:
# ["flower", "flow", "flight"] → "fl"

def longest_common_prefix(strs):
    if not strs:
        return ""

    shortest_str = min(strs, key=len)

    for i, c in enumerate(shortest_str):
        for s in strs:
            if shortest_str[i] != s[i]:
                return shortest_str[:i]

    return shortest_str

print("Longest common prefix solution:")
print(longest_common_prefix(["flower", "flow", "flight"]))

# ---
#
# ### 2. Compress a String
#
# Given a string, compress it by counting consecutive repeated characters.
#
# Example idea:
# "aabcc" → "a2b1c2"

def str_compress(s):
    c = 1
    result = ""
    for i in range (1, len(s)):
        if s[i-1] == s[i]:
            c += 1
        else:
            result += s[i-1] + str(c)
            c = 1
    result += s[-1] + str(c)

    return result

print("\nString compression solution:")
print(str_compress("aabcc"))


# ### 3. Count Vowels and Consonants
#
# Given a string, count:
# - the number of vowels (a, e, i, o, u),
# - and the number of consonants (all other alphabet letters).
#
# Ignore non-letter characters if necessary.

def count_alphabets(s):
    total_char = 0
    vowel_count = 0
    for c in s:
        if c.isalpha():
            total_char += 1
            if c.lower() in "aeiou":
                vowel_count += 1

    return vowel_count, total_char - vowel_count

print("\nSolution for vowel and consonat count:")
print(count_alphabets("aa3434 cat"))


# ### 4. Check Balanced Parentheses
#
# Given a string containing parentheses (such as (), [], {}), determine whether they are properly balanced.
#
# Balanced means:
# - every opening symbol has a matching closing symbol,
# - and they close in the correct nested order.

def balanced_parentheses(s):
    stack = []
    map = {")": "(", "}": "{", "]": "["}
    for c in s:
        if c in "({[":
            stack.append(c)
        if c in ")}]":
            if not stack:
                return False
            if stack[-1] != map[c]:
                return False
            stack.pop()
    return not stack

print("\nBalanced parentheses output:")
print(balanced_parentheses("(((({{{)))()()"))
print(balanced_parentheses("({[]})"))


# ### 5. Longest Substring Without Repeating Characters (medium)
#
# Given a string, find the longest continuous substring that contains no repeated characters.
#
# Example idea:
# "abcabcbb" → "abc" (length 3)
def longest_substr(s):
    left = 0
    seen = set()
    best_start, best_len = 0, 0

    for right, c in enumerate(s):


print("\nSolution for the longest substring:")
print(longest_substr("abcabcbb"))

