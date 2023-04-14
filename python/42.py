class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left, right = [0]*n, [0]*n
        left[0], right[n-1] = height[0], height[n-1]
        
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
            
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
            
        ans = 0
        for i in range(n):
            ans += min(left[i], right[i]) - height[i]
            
        return ans