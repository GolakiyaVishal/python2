"""
https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

A non-empty array A consisting of N integers is given. 
The array contains an odd number of elements, 
and each element of the array can be paired with another element that has the same value, 
except for one element that is left unpaired.
"""

def solution(A):
    stack = []
    for e in A:
        if e in stack:
            stack.remove(e)
        else:
            stack.append(e)
    
    if len(stack) > 0:
        return stack[0]
    else:
        return -1

if __name__ == '__main__':
    print(solution([9,8,9,8,9]))