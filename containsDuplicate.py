class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        print(nums)
        prev:int = -9999999999
        for num in nums:
            if prev == num:
                return True
            prev = num
        return False