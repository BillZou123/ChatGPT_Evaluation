public class Solution {
    public IList<IList<int>> PermuteUnique(int[] nums) {
        IList<IList<int>> result = new List<IList<int>>();
        Array.Sort(nums);
        Backtrack(result, new List<int>(), nums, new bool[nums.Length]);
        return result;
    }
    
    private void Backtrack(IList<IList<int>> result, List<int> tempList, int[] nums, bool[] used) {
        if(tempList.Count == nums.Length) {
            result.Add(new List<int>(tempList));
        } else {
            for(int i = 0; i < nums.Length; i++) {
                if(used[i] || (i > 0 && nums[i] == nums[i-1] && !used[i-1])) continue;
                used[i] = true;
                tempList.Add(nums[i]);
                Backtrack(result, tempList, nums, used);
                used[i] = false;
                tempList.RemoveAt(tempList.Count - 1);
            }
        }
    }
}