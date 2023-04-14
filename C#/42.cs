public class Solution {
    public int Trap(int[] height) {
        int n = height.Length;
        if(n == 0) return 0;
        int left = 0, right = n-1;
        int leftMax = height[left], rightMax = height[right];
        int ans = 0;
        while(left < right){
            if(height[left] < height[right]){
                if(height[left] > leftMax) leftMax = height[left];
                else ans += leftMax - height[left];
                left++;
            }else{
                if(height[right] > rightMax) rightMax = height[right];
                else ans += rightMax - height[right];
                right--;
            }
        }
        return ans;
    }
}