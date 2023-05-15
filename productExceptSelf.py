from ast import List

def productExceptSelf(nums: List) -> List:
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        print(res)
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        print(res)
        res[i] *= postfix
        postfix *= nums[i]

    return res

print(productExceptSelf([1,2,3,4]))