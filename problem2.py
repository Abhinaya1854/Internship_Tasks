# https://www.hackerrank.com/challenges/py-the-captains-room/problem
k = int(input())
room_list = list(map(int, input().split()))
room_set = set(room_list)
captains_room = ((sum(room_set) * k) - sum(room_list)) // (k - 1)
print(captains_room)
