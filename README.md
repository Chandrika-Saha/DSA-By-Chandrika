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
