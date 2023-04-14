public class Solution {
    public int ThreeSumClosest(int[] nums, int target) {
        Array.Sort(nums);
        int closestSum = nums[0] + nums[1] + nums[2];
        for(int i = 0; i < nums.Length - 2; i++){
            int left = i + 1, right = nums.Length - 1;
            while(left < right){
                int sum = nums[i] + nums[left] + nums[right];
                if(sum == target) return sum;
                if(Math.Abs(sum - target) < Math.Abs(closestSum - target)){
                    closestSum = sum;
                }
                if(sum < target){
                    left++;
                }else{
                    right--;
                }
            }
        }
        return closestSum;
    }
}