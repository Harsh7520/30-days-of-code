class Solution:
   def solve(self, s):
      ans = 0
      for c in map(int, s):
         ans = 3 * ans + c
      return ans
ob = Solution()
print(ob.solve(input()))
