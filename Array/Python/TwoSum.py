class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}

        for i,num in enumerate(nums):
            if num in dict:
                return[dict[num],i]
            else:
                dict[target-num]=i 

mySol = Solution()
print(mySol.twoSum([2,7,11,15],9))
print(mySol.twoSum([3,2,4],6))
print(mySol.twoSum([3,3],6))