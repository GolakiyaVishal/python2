from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        if len(nums) <= 1:
            return 0
        nums.sort()
        count = 0
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums) and (nums[i] + nums[j]) < target:
                print(f'{i},{j} = {nums[i]},{nums[j]}')
                count += 1
                j += 1
          
        
        return count
    
if __name__ == '__main__':
    print(Solution().countPairs([-6,2,5,-2,-7,-1,3], 14))
    # print(Solution().countPairs([6,-1,7,4,2,3], 8))
    # print(Solution().countPairs([-8,-9,-10,0,-5,-5], -15))
    # print(Solution().countPairs([-5,-4,-10,7], 14))