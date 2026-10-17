# https://www.hackerrank.com/challenges/piling-up/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        blocks = list(map(int, input().split()))
        
        left = 0
        right = n - 1
        current_top = float('inf')  
        possible = True
        while left <= right:
            if blocks[left] >= blocks[right]:
                picked = blocks[left]
                left += 1
            else:
                picked = blocks[right]
                right -= 1
            if picked > current_top:
                possible = False
                break
                
            current_top = picked
        if possible:
            print("Yes")
        else:
            print("No")
