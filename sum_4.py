from typing import List

def sumFour(nums:List[int], target: int) -> List[List[int]]:
    nums.sort()
    data = []
    l = len(nums)

    for i in range(l-3):
        tl = nums[i:i+3]
        for j in range(i+3,l):
            tl.append(nums[j])
            if sum(tl) == target:
                data.append(tl)
            tl.pop(-1)
    
    return data

if __name__=='__main__':
    print(sumFour([1,0,-1,0,-2,2], 0))