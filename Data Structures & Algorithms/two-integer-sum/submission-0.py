class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, number in enumerate(nums):
            need = target - number

            if need in seen:
                 return [seen[need], i]

            seen[number] = i
            
        
        

