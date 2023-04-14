class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, isLeft):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    if isLeft:
                        if mid == 0 or nums[mid-1] != target:
                            return mid
                        else:
                            right = mid - 1
                    else:
                        if mid == len(nums)-1 or nums[mid+1] != target:
                            return mid
                        else:
                            left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        leftIndex = binarySearch(nums, target, True)
        if leftIndex == -1:
            return [-1, -1]
        rightIndex = binarySearch(nums, target, False)
        return [leftIndex, rightIndex]