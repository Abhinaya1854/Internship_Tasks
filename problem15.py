# Problem: Word Order
# HackerRank: https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# Read the number of words
n = int(input())

# Read all words into a list
words = [input().strip() for _ in range(n)]

# Count occurrences while preserving insertion order
word_counts = Counter(words)

# Line 1: Print the number of distinct words
print(len(word_counts))

# Line 2: Print the counts separated by a space
print(*(word_counts.values()))