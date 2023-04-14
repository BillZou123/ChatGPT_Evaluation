class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == n:
                res.append(nums[:])
            used = set()
            for i in range(start, n):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
        
        n = len(nums)
        res = []
        backtrack(0)
        return res