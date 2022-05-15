class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            try:
                d[i]+=1
                return i
            except:
                d[i]=1
