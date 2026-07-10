class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0

        numSet = set(nums)

        for n in numSet:
            if n-1 not in numSet:
                lenght = 0
                while n+lenght in numSet:
                    lenght += 1
                longest = max(longest, lenght)


        return longest
        