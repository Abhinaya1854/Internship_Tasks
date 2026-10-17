# https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        command_args = input().split()
        command = command_args[0]
        
        if command == "print":
            print(my_list)
        elif command == "insert":
            my_list.insert(int(command_args[1]), int(command_args[2]))
        elif command == "append":
            my_list.append(int(command_args[1]))
        elif command == "remove":
            my_list.remove(int(command_args[1]))
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            my_list.pop()
        elif command == "reverse":
            my_list.reverse()
