public class Solution {
    public IList<IList<int>> CombinationSum2(int[] candidates, int target) {
        Array.Sort(candidates);
        IList<IList<int>> result = new List<IList<int>>();
        FindCombinations(candidates, target, 0, new List<int>(), result);
        return result;
    }
    
    private void FindCombinations(int[] candidates, int target, int start, IList<int> currList, IList<IList<int>> result){
        if(target == 0){
            result.Add(new List<int>(currList));
            return;
        }
        for(int i=start; i<candidates.Length && candidates[i]<=target; i++){
            if(i>start && candidates[i]==candidates[i-1]) continue;
            currList.Add(candidates[i]);
            FindCombinations(candidates, target-candidates[i], i+1, currList, result);
            currList.RemoveAt(currList.Count-1);
        }
    }
}