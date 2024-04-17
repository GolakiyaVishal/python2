"""
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
"""
from typing import List

class Solution:
    def countNegative(self, grid: List[List[int]]):
        count, r, c, grid_length = 0, 0, len(grid[0])-1, len(grid)

        while r < grid_length and c >= 0:
            if grid[r][c] < 0:
                count += grid_length - r
                c -= 1
            else:
                r += 1
        
        return count
    
if __name__ == '__main__':
    # print(Solution().countNegative([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
    print(Solution().countNegative([[3,2],[1,0]]))