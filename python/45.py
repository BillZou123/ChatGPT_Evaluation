class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        jumps = 1
        curr_end = nums[0]
        next_end = nums[0]
        
        for i in range(1, len(nums)):
            if i > curr_end:
                jumps += 1
                curr_end = next_end
            
            next_end = max(next_end, i + nums[i])
        
        return jumps