# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
_ = input()
english_subs = set(map(int, input().split()))
_ = input()
french_subs = set(map(int, input().split()))
either_but_not_both = english_subs.symmetric_difference(french_subs)
print(len(either_but_not_both))
