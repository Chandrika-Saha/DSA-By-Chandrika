# Two Sum: given a list of integers and a target integer, return the indices of the
# two numbers that add up to the target.
def two_sum(nums, target):
    num_dict = {}
    for i, n in enumerate(nums):
        if (target - n) in num_dict:
            return num_dict[(target - n)], i
        num_dict[n] = i

    return None

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [3, 2, 4]
target = 6
print(two_sum(nums, target))

nums = [3, 3]
target = 6
print(two_sum(nums, target))


# Given an array, move all the zeros to the end while keeping the relative order of
# non-zero elements the same.
def move_zeros_to_end(nums):
    c_non_zeros = 0

    for n in nums:
        if n != 0:
            nums[c_non_zeros] = n
            c_non_zeros += 1

    for i in range(c_non_zeros, len(nums)):
        nums[i] = 0
    return nums



nums = [0, 1, 0, 3, 12]
print(move_zeros_to_end(nums))

nums = [1, 2, 3, 4, 0, 0, 0]
print(move_zeros_to_end(nums))

nums = [0, 0, 0, 0]
print(move_zeros_to_end(nums))

nums = [1, 2, 3, 4, 5]
print(move_zeros_to_end(nums))

nums = [4, 8, 0, 0, 2, 0, 1, 0]
print(move_zeros_to_end(nums))


# Find missing numbers in 1...n. You get a list containing n distinct numbers, but instead of containing all numbers
# from 1 to n, one number is missing, figure out the missing numbers
def find_missing_number(arr, n):
    expected_sum = n * (n + 1)/2
    return int(expected_sum - sum(arr))

print(find_missing_number([1, 2, 4, 5], 5))
print(find_missing_number([7, 1, 2, 4, 6, 3], 7))
print(find_missing_number([2, 3, 4], 4))

# Kadane's algorithm: given an array of positive and negative integers, find the maximum possible sum of
# a continuous subarray
def kadanes(arr):

    max_total = float('-inf')
    sub_array_sum = 0
    for i, n in enumerate(arr):
        if (sub_array_sum + n) > n:
            sub_array_sum += n
        else:
            sub_array_sum = n
        if max_total < sub_array_sum:
            max_total = sub_array_sum
    return max_total

print("\nKaden's results:")
print(kadanes([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(kadanes([1, 2, 3, 4]))
print(kadanes([-5, -2, -7, -1, -3]))
print(kadanes([8]))

# Rotate array by k steps: You need to shift all elements to the right by k position
# Elements that "fall off" the end should wrap around to the front
def rotate_arr_by_k(arr, k):
    k = k % len(arr)
    # arr[-k:] is the last k elements and arr[:-k] is everything except last two elements
    return arr[-k:] + arr[:-k]

print(rotate_arr_by_k([1, 2, 3, 4, 5], 2))