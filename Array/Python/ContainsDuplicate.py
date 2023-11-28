class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict = {}
        for i, num in enumerate(nums):
            if num in dict:
                return True
            else:
                dict[num] = 1
        return False
    

mySol = Solution()
print(mySol.containsDuplicate([1,2,3,1]))
print(mySol.containsDuplicate([1,2,3,4]))
print(mySol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))