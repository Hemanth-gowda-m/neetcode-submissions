class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pervMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in pervMap:
                return [pervMap[diff],i]
            pervMap[nums[i]] = i
        
        return
        