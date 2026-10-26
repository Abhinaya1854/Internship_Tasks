
# Q1. Find the frequency of each word
def q1_word_frequency(sentence):
    frequency = {}
    for word in sentence.split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


# Q2. Find the frequency of each character
def q2_character_frequency(word):
    frequency = {}
    for char in word:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


# Q3. Find the first non-repeating character
def q3_first_non_repeating(word):
    frequency = {}
    for char in word:
        frequency[char] = frequency.get(char, 0) + 1

    for char in word:
        if frequency[char] == 1:
            return char
    return None


# Q4. Check whether two strings are anagrams
def q4_are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)


# Q5. Find the first repeating character
def q5_first_repeating(word):
    seen = set()
    for char in word:
        if char in seen:
            return char
        seen.add(char)
    return None


# Q6. Move all zeros to the end
def q6_move_zeros(nums):
    result = []
    for num in nums:
        if num != 0:
            result.append(num)

    zeros = len(nums) - len(result)
    result.extend([0] * zeros)
    return result


# Q7. Find the second-highest distinct number
def q7_second_highest(nums):
    unique = sorted(set(nums))
    if len(unique) < 2:
        return None
    return unique[-2]


# Q8. Remove duplicates while preserving order
def q8_remove_duplicates(nums):
    result = []
    seen = set()

    for num in nums:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result


# Q9. Find the missing number from 1 to N
def q9_missing_number(nums, n):
    total = n * (n + 1) // 2
    return total - sum(nums)


# Q10. Find the first pair whose sum equals target
def q10_two_sum(nums, target):
    for j in range(len(nums)):
        for i in range(j):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return []


# Q11. Find the number closest to zero
def q11_closest_to_zero(nums):
    return min(nums, key=lambda x: (abs(x), -x))


# Q12. Find common elements between two lists
def q12_common_elements(list1, list2):
    second = set(list2)
    result = []
    seen = set()

    for num in list1:
        if num in second and num not in seen:
            result.append(num)
            seen.add(num)
    return result


# Q13. Rotate a list to the right by K positions
def q13_rotate_right(nums, k):
    if not nums:
        return []

    k = k % len(nums)
    return nums[-k:] + nums[:-k] if k else nums[:]


# Q14. Find the maximum sum of consecutive elements
def q14_max_consecutive_sum(nums):
    maximum = nums[0] + nums[1]

    for i in range(1, len(nums) - 1):
        current = nums[i] + nums[i + 1]
        if current > maximum:
            maximum = current
    return maximum


# Q15. Find all unique pairs whose sum equals target
def q15_all_pairs(nums, target):
    pairs = set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = tuple(sorted((nums[i], nums[j])))
                pairs.add(pair)

    return [list(pair) for pair in sorted(pairs)]

