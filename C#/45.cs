public class Solution {
    public int Jump(int[] nums) {
        int n = nums.Length;
        int jumps = 0;
        int currEnd = 0;
        int currFarthest = 0;
        
        for (int i = 0; i < n - 1; i++) {
            currFarthest = Math.Max(currFarthest, i + nums[i]);
            if (i == currEnd) {
                jumps++;
                currEnd = currFarthest;
            }
        }
        
        return jumps;
    }
}