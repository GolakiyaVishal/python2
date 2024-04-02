from typing import List

def solution(arr: List[int], sub: List[int]):
    arr_idx = 0
    sub_idx = 0

    while arr_idx < len(arr) and sub_idx < len(sub):
        if arr[arr_idx] == sub[sub_idx]:
            sub_idx += 1
            if sub_idx == len(sub):
                return True
        arr_idx += 1
    
    return False

if __name__ == '__main__':
    print(solution([1,2,3,4,5,6,7,8],[9]))