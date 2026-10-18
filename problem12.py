# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())
for _ in range(num_commands):
    command = input().split()
    operation = command[0]
    
    if operation == "pop":
        s.pop()
    elif operation == "remove":
        s.remove(int(command[1]))
    elif operation == "discard":
        s.discard(int(command[1]))
print(sum(s))
