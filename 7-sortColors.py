from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        x=Counter(nums)
        y=[0,1,2]
        ans=[]
        nums.clear()
        for col in y:
            for i in range(x[col]):
                nums.append(col)
