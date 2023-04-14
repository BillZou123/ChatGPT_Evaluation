public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        int left = 0;
        int right = nums.Length - 1;
        int[] result = new int[2];
        result[0] = -1;
        result[1] = -1;
        
        // binary search to find the starting position of target
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target && (mid == 0 || nums[mid-1] != target)) {
                result[0] = mid;
                break;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        // binary search to find the ending position of target
        left = 0;
        right = nums.Length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target && (mid == nums.Length - 1 || nums[mid+1] != target)) {
                result[1] = mid;
