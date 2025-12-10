# String reverse
string = input("Enter a string: ")
print(f"reversed: {string[::-1]}")

# Check if string is palindrome
string = input("Enter a string to check palindrome: ")
string = string.lower().replace(" ", "")
result = "The string is palindrom" if string == string[::-1] else "The string is not a palindrome"
print(result)

# Find the max min in a list
lst = [9, 2, 4, 5, 5, 5, 3, 2]
print(f"Max number in the list is {max(lst)}\nMin number in the list is {min(lst)}")

# Remove duplicates from a list
lst_r_d = list(set(lst))
print(f"After removing all the duplicates the list is: {lst_r_d}")

seen = set()
without_d = [l for l in lst if not (l in seen or seen.add(l))]
print(f"After removing all the duplicates the list is: {without_d}")

# Count frequency of characters in a string (use dict)
string = input("Enter a string to count frequency of characters in that string: ")
s_dict = {}
for c in string:
    s_dict[c] = s_dict.get(c, 0) + 1
print(f"Character count dict: {s_dict}")

from collections import Counter
print(f"Character count dict: {Counter(string)}")

# Merge two sorted lists
lst1 = [1, 3, 5, 7, 9]
lst2 = [2, 4, 6, 6, 8, 10, 10]

ptr1, ptr2 = 0, 0
merged_lst = []

while ptr1 < len(lst1) and ptr2 < len(lst2):
    if lst1[ptr1] < lst2[ptr2]:
        merged_lst.append(lst1[ptr1])
        ptr1 += 1
    else:
        merged_lst.append(lst2[ptr2])
        ptr2 += 1

merged_lst.extend(lst1[ptr1:])
merged_lst.extend(lst2[ptr2:])

print(f"the merged list is: {merged_lst}")


# Find the index of the first occurrence of an element
lst3 = [8, 5, 5, 7, 5]
def first_index(lst, v):
    return next((i for i, l in enumerate(lst) if l == v), -1)

print(f"Index of the first occurrence of 5 in the list is {lst3.index(5)}")
print(f"Index of the first occurrence of 5 in the list is {first_index(lst3, 5)}")


# Check if two string are anagrams
str1, str2 = "car", "rac"
str3, str4 = "hello", "bello"
def check_anagrams(str1, str2):
    return "They are anagrams" if Counter(str1) == Counter(str2) else "They are not anagrams"
    # return "They are anagrams" if  (len(str1) == len(str2) and sorted(str1) == sorted(str2)) else "They are not anagrams"
print(f"str1 and str2: {check_anagrams(str1, str2)}")
print(f"str3 and str4: {check_anagrams(str3, str4)}")

# Return even numbers from a list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst_even = [l for l in lst if l%2 == 0]
print(f"Only even numbers: {lst_even}")


# Compute factorial
n = int(input("Enter a number to compute factorial: "))
result = 1
for i in range(2, n+1):
    result *= i
print(f"The factorial of {n} is {result}")


