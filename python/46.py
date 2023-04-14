class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            result = []
            for i in range(len(nums)):
                remaining_list = nums[:i] + nums[i+1:]
                for perm in self.permute(remaining_list):
                    result.append([nums[i]] + perm)
            return result