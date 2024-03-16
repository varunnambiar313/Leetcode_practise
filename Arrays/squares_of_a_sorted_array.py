class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        j = len(nums)-1
        while i!=j:
            if i>j:
                break
            if abs(nums[i])>abs(nums[j]):
                result = [nums[i]**2]+result
                i+=1
            elif abs(nums[i])<abs(nums[j]):
                result = [nums[j]**2]+result
                j-=1
            else:
                result = [nums[j]**2]+result
                result = [nums[i]**2]+result
                i+=1
                j-=1
        if i==j:
            result = [nums[i]**2]+result
        return result
                
