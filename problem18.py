# https://www.hackerrank.com/challenges/py-set-mutations/problem
num_elements_a = int(input())
set_a = set(map(int, input().split()))
num_operations = int(input())

for _ in range(num_operations):
    operation_name = input().split()[0]
    other_set = set(map(int, input().split()))
    getattr(set_a, operation_name)(other_set)
print(sum(set_a))