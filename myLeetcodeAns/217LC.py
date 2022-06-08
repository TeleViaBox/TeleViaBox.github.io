# STATUS: not yet finished!
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        index = 0
        check = []*len(nums)
        for i in range(0, len(nums)):
            check[index] = nums[i]
            for j in range(0, len(check)):
                if check[j] == nums[i]:
                    return false
            index += 1
        return true
            
