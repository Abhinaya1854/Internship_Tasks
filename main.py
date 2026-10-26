
from solutions import (
    q1_word_frequency,
    q2_character_frequency,
    q3_first_non_repeating,
    q4_are_anagrams,
    q5_first_repeating,
    q6_move_zeros,
    q7_second_highest,
    q8_remove_duplicates,
    q9_missing_number,
    q10_two_sum,
    q11_closest_to_zero,
    q12_common_elements,
    q13_rotate_right,
    q14_max_consecutive_sum,
    q15_all_pairs
)

# Q1: Word frequency
print("Q1:", q1_word_frequency(
    "python is easy and python is powerful"))
print("Q1 Extra:", q1_word_frequency("hi hello hi"))

# Q2: Character frequency
print("Q2:", q2_character_frequency("banana"))
print("Q2 Extra:", q2_character_frequency("apple"))

# Q3: First non-repeating character
print("Q3:", q3_first_non_repeating("swiss"))
print("Q3 Extra:", q3_first_non_repeating("aabb"))

# Q4: Anagrams
print("Q4:", q4_are_anagrams("listen", "silent"))
print("Q4 Extra:", q4_are_anagrams("hello", "world"))

# Q5: First repeating character
print("Q5:", q5_first_repeating("programming"))
print("Q5 Extra:", q5_first_repeating("abc"))

# Q6: Move zeros
print("Q6:", q6_move_zeros([0, 3, 0, 1, 2, 0, 4]))
print("Q6 Extra:", q6_move_zeros([0, 1, 0, 2]))

# Q7: Second-highest distinct number
print("Q7:", q7_second_highest([10, 20, 40, 30, 40, 20]))
print("Q7 Extra:", q7_second_highest([5, 5, 5]))

# Q8: Remove duplicates
print("Q8:", q8_remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8 Extra:", q8_remove_duplicates([1, 1, 2, 3, 2]))

# Q9: Missing number
print("Q9:", q9_missing_number([1, 2, 4, 5, 6], 6))
print("Q9 Extra:", q9_missing_number([1, 3, 4], 4))

# Q10: First pair with target sum
print("Q10:", q10_two_sum([2, 7, 11, 15], 9))
print("Q10 Extra:", q10_two_sum([1, 4, 6], 20))

# Q11: Number closest to zero
print("Q11:", q11_closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11 Extra:", q11_closest_to_zero([-7, -1, 4]))

# Q12: Common elements
print("Q12:", q12_common_elements(
    [1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 Extra:", q12_common_elements(
    [1, 2, 2, 3], [2, 3, 4]))

# Q13: Rotate right
print("Q13:", q13_rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 Extra:", q13_rotate_right([1, 2, 3], 1))

# Q14: Maximum consecutive sum
print("Q14:", q14_max_consecutive_sum([4, 7, 2, 9, 5]))
print("Q14 Extra:", q14_max_consecutive_sum([1, 10, 2]))

# Q15: All unique pairs
print("Q15:", q15_all_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 Extra:", q15_all_pairs([1, 2, 3, 4], 5))
