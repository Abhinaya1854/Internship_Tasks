
# Problem: Nested Lists
# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students = []
    
    # Read the number of students and their details in ONE loop
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    # Your correct logic continues here:
    scores = sorted(set(student[1] for student in students))
    second_lowest = scores[1]
    
    names = sorted(
        student[0]
        for student in students
        if student[1] == second_lowest
    )
    
    for name in names:
        print(name)