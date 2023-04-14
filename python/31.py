class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the first decreasing element from right to left
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # if no decreasing element is found, reverse the whole array
        if i < 0:
            nums.reverse()
        else:
            # find the smallest element greater than the decreasing element
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            # swap the two elements
            nums[i], nums[j] = nums[j], nums[i]
            # reverse the subarray to the right of the decreasing element
            nums[i+1:] = reversed(nums[i+1:])