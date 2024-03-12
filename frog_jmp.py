"""
https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

A small frog wants to get to the other side of the road. 
The frog is currently located at position X and wants to get to a position greater than or equal to Y. 
The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.
"""

def solution(X, Y, D):
    fd = Y-X
    if (fd <= 0):
        return 0
    j = fd % D
    if( j == 0):
        return round(fd / D)
    return round((fd / D) + 0.5)

if __name__ == '__main__':
    print(solution(2, 11, 3))
