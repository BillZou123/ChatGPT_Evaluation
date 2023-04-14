class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n-1)
        count = 1
        curr = ""
        for i in range(len(prev)):
            if i == len(prev)-1 or prev[i] != prev[i+1]:
                curr += str(count) + prev[i]
                count = 1
            else:
                count += 1
        return curr