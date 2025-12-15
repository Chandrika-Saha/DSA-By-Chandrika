# DSA-By-Chandrika

A curated collection of data structures and algorithms practice problems, organized by difficulty.  
This repository serves as my structured preparation for coding interviews and assessments.

---

## 📌 Section 1 — Warm-Up (Easy)

Foundational problems to build comfort with strings, lists, loops, and dictionaries.

### ✔ Problems Completed

- Reverse a string  
- Check if a string is a palindrome  
- Find the maximum and minimum in a list  
- Remove duplicates while preserving order  
- Count frequency of characters in a string (dictionary)  
- Merge two sorted lists  
- Find the index of the first occurrence of an element  
- Check if two strings are anagrams  
- Return even numbers from a list  
- Compute factorial (iterative)

# SECTION 2 — Core Problems 
## 1. Two Sum (classic)

You are given an array of integers and a target number.
You must find two different numbers in the array that add up to the target.
Return their indices.

Important:
- You cannot use the same element twice.
- There is always either one valid pair or none (depending on the version).

---

## 2. Move Zeros to the End

Given an array, shift all zero values to the end of the array, while:
- Keeping the order of all the non-zero numbers the same.
- Doing it in-place (modify the original array).

The array length stays the same; only positions change.

---

## 3. Find Missing Number in 1..n

You get a list containing n distinct numbers, but instead of containing all numbers from 1 to n, one number is missing.
Your task: figure out which number is missing.

Example:
If n = 5, the numbers should be [1, 2, 3, 4, 5], but one is absent.

---

## 4. Kadane’s Algorithm (Max Subarray Sum) – medium

Given an array of positive and negative integers, find the maximum possible sum of a continuous subarray.

Example:
In [-2, 1, -3, 4, -1, 2, 1, -5, 4], the best continuous section is [4, -1, 2, 1] because it has the highest sum.

You are not asked to implement Kadane’s algorithm specifically — just find the max sum.

---

## 5. Rotate Array by k Steps

You have an array and a number k.
You need to shift all elements to the right by k positions.
Elements that “fall off” the end should wrap around to the front.

Example:
Rotating [1, 2, 3, 4, 5] by k = 2 → [4, 5, 1, 2, 3]

## Strings — Additional Core Problems

---

### 1. Longest Common Prefix

Given a list of strings, find the longest starting substring (prefix) that all strings share.

Example idea:
["flower", "flow", "flight"] → "fl"

---

### 2. Compress a String

Given a string, compress it by counting consecutive repeated characters.

Example idea:
"aabcc" → "a2b1c2"

This is similar to simple run-length encoding.

---

### 3. Count Vowels and Consonants

Given a string, count:
- the number of vowels (a, e, i, o, u),
- and the number of consonants (all other alphabet letters).

Ignore non-letter characters if necessary.

---

### 4. Check Balanced Parentheses

Given a string containing parentheses (such as (), [], {}), determine whether they are properly balanced.

Balanced means:
- every opening symbol has a matching closing symbol,
- and they close in the correct nested order.

---

### 5. Longest Substring Without Repeating Characters (medium)

Given a string, find the longest continuous substring that contains no repeated characters.

Example idea:
"abcabcbb" → "abc" (length 3)

## HashMaps/Sets — Additional Core Problems

### 1. First Non-Repeating Character

Given a string, find the first character that does **not** repeat anywhere else in the string.

Example:
- "swiss" → "w"

Use a hash map to count frequencies, then scan again to find the first char with count == 1.


### 2. Find Duplicates in an Array

Given an array, return all values that appear **more than once**.

Example:
- [1,2,3,1,5,2] → duplicates: [1,2]

A hash set or hash map helps detect repeated elements efficiently.


### 3. Intersection of Two Lists

Given two lists, return the elements that appear in **both**.

Example:
- A = [1,2,3,4]
- B = [2,4,6]
- Intersection = [2,4]

Use a set for fast membership checking.


### 4. Group Anagrams (medium)

Given a list of words, group together all words that are **anagrams** of each other.

Example:
Input: ["eat","tea","tan","ate","nat","bat"]  
Output:
[
  ["eat","tea","ate"],
  ["tan","nat"],
  ["bat"]
]

Anagrams share the same sorted characters, so they map to the same key in a hash map.


### 5. Word Frequency Counter

Given a block of text, count how many times each **word** appears.

Example:
- "cat dog cat mouse" → {cat: 2, dog: 1, mouse: 1}

A hash map is ideal for counting occurrences.

