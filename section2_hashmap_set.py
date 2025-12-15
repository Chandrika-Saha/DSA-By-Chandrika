# ### 1. First Non-Repeating Character
#
# Given a string, find the first character that does **not** repeat anywhere else in the string.
#
# Example:
# - "swiss" → "w"


def first_unique(s):

    map_c = {}
    for c in s:
        map_c[c] = map_c.get(c, 0) + 1

    for c in s:
        if map_c[c] == 1:
            return c

    return ""

print("Solution for the first unique character in a string:")
print(first_unique("swiss"))



#
# ### 2. Find Duplicates in an Array
#
# Given an array, return all values that appear **more than once**.
#
# Example:
# - [1,2,3,1,5,2] → duplicates: [1,2]
#
# A hash set or hash map helps detect repeated elements efficiently.

def find_duplicates_list(arr):
    if not arr:
        return arr
    counts = {}
    for n in arr:
        counts[n] = counts.get(n, 0) + 1

    result = [n for n, c in counts.items() if counts[n] > 1]

    return result

print("\nSolution for find duplicates in a list:")
print(find_duplicates_list([1, 2, 1, 2, 3, 4, 5, 6]))
#
# ### 3. Intersection of Two Lists
#
# Given two lists, return the elements that appear in **both**.
#
# Example:
# - A = [1,2,3,4]
# - B = [2,4,6]
# - Intersection = [2,4]
#
# Use a set for fast membership checking.

def list_intersection(l1, l2):
    l2_s = set(l2)
    result = []
    seen = set()
    for n in l1:
        if n in l2_s and n not in seen:
            result.append(n)
            seen.add(n)
    return result

    # # Where the order doesn't matter
    # return list(set(l1).intersection(set(l2)))
print("\nSolution for list intersection:")
print(list_intersection([1, 2, 3, 4], [2, 4, 6]))
#
# ### 4. Group Anagrams (medium)
#
# Given a list of words, group together all words that are **anagrams** of each other.
#
# Example:
# Input: ["eat","tea","tan","ate","nat","bat"]
# Output:
# [
#   ["eat","tea","ate"],
#   ["tan","nat"],
#   ["bat"]
# ]
#
# Anagrams share the same sorted characters, so they map to the same key in a hash map.

def group_anagrams(s_arr):
    maps = {}
    for s in s_arr:
        s_sorted = ''.join(sorted(s))
        maps.setdefault(s_sorted, []).append(s)

    return list(maps.values())
print("\nSolution for grouping anagrams:")
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
#
# ### 5. Word Frequency Counter
#
# Given a block of text, count how many times each **word** appears.
#
# Example:
# - "cat dog cat mouse" → {cat: 2, dog: 1, mouse: 1}
#
# A hash map is ideal for counting occurrences.

def word_frequency_counter(s):
    result = {}
    for word in s.split():
        result[word] = result.get(word, 0) + 1
    return result

print("\nSolution for word counter:")
print(word_frequency_counter("cat dog cat mouse"))
