public class Solution {
    public string CountAndSay(int n) {
        if(n == 1) return "1";
        string prev = CountAndSay(n-1);
        string result = "";
        int count = 1;
        for(int i=0; i<prev.Length; i++){
            if(i == prev.Length-1 || prev[i] != prev[i+1]){
                result += count.ToString() + prev[i];
                count = 1;
            }
            else{
                count++;
            }
        }
        return result;
    }
}