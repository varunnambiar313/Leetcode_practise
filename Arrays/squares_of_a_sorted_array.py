class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        poppers=[]
        for i in range(len(nums)):
            if nums[i]<0:
                for j,k in reversed(list(enumerate(nums))):
                    if abs(nums[i])>nums[j]:
                        nums.insert(j+1,abs(nums[i]))
                        poppers.append(int(i))
                        break
        for p in range(len(poppers)):
            nums.pop(0)
        for o in range(len(nums)):
            nums[o] = nums[o]**2
        return nums
