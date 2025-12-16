# 1. Lists (arrays)
#
# ⭐ Implement your own versions of:
#
# append, insert(index, value), pop(index) using slicing (don’t call the built-ins).
#

class ListMine:
    def __init__(self):
        self.lst = []

    def append_mine(self, item):
        new_lst = [item]
        self.lst = self.lst + new_lst

    def insert_mine(self, index, value):
        if index < 0:
            index = len(self.lst) + index

        if index > len(self.lst):
            raise IndexError("Index out of range")

        temp = self.lst[:index] + [value] + self.lst[index:]
        self.lst = temp

    def pop_mine(self, index):

        if not self.lst:
            raise IndexError("Pop from empty list")

        if index < 0:
            index = len(self.lst) + index

        if index < 0 or index >= len(self.lst):
            raise IndexError("Index out of range")

        value = self.lst[index]
        temp = self.lst[:index] + self.lst[index+1:]
        self.lst = temp
        return value

    def __str__(self):
        return str(self.lst)

lst = ListMine()
lst.append_mine(1)
lst.append_mine(2)
lst.append_mine(3)
print(lst)

lst.insert_mine(1, 600)
lst.insert_mine(3, 900)
print(lst)

lst.pop_mine(2)
lst.pop_mine(0)
print(lst)

# lst.pop_mine(34)
# lst.insert_mine(343, 54545)


# ⭐ Reverse a list in place without using reversed() or list[::-1].

lst = [1, 2, 3, 4, 5]
print("Before reverse:", lst)

n = len(lst) // 2
last_idx = len(lst) - 1
for i in range(n):
    last_idx -= i
    lst[i], lst[last_idx] = lst[last_idx], lst[i]
    print(lst)

print("After reverse:", lst)
#
# ⭐ Remove duplicates from a list while preserving order.

lst = [1, 1, 1, 2, 3, 4, 5, 2, 3, 5]
seen = set()
result = []
for n in lst:
    if n not in seen:
        seen.add(n)
        result.append(n)
print("Without duplicates:", result)
#
# ⭐ Rotate a list to the right by k steps. (e.g., [1,2,3,4,5], k=2 → [4,5,1,2,3])
lst = [1, 2, 3, 4, 5]
k = 3
lst = lst[-k:] + lst[:-k]
print("Rotated list:", lst)
#
# ⭐ Given a sorted list, remove duplicates in place and return the new length.
lst = [1, 1, 1, 2, 2, 3]
write = 1
for read in range(1, len(lst)):
    if lst[read - 1] != lst[read]:
        lst[write] = lst[read]
        write += 1
print("Sorted list without duplicates, in place", lst[:write])
print("How many ", write)
#
# ⭐⭐ Given a list of integers and a target sum, return indices of two numbers that add up to the target (the classic Two Sum).
#
# ⭐⭐ Implement:
#
# intersection of two lists, preserving order of the first
#
# union of two lists with unique elements
#
# ⭐⭐ Sliding window:
#
# Given a list of integers and k, find the max sum of any subarray of length k.
#
# ⭐⭐ Given a list of 0s, 1s, and 2s, sort it in one pass (Dutch National Flag).
#
# ⭐⭐ Matrix practice (list of lists):
#
# Transpose a matrix.
#
# Rotate a matrix 90 degrees clockwise.
#
# ⭐⭐⭐ Given a list of integers, find the length of the longest increasing subsequence (LIS) – optimize beyond O(n²) if you want a challenge.
#
# ⭐⭐⭐ Implement merge of k sorted lists into one sorted list (first with simple merging, later with heap).