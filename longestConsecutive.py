from ast import List

def longestConsecutive(nums: List) -> int:
    if len(nums) == 0:
        return 0    
    if len(nums) == 1:
        return 1   
    current = 0
    next = 1
    nums = sorted(list(set(nums)))
    print(nums)
    consecutive_count = []
    counter = 0
    for _ in range(len(nums) - 1):
        print(nums[next] - nums[current])
        if (nums[next] - nums[current] == 1):
            counter += 1
        else:
            consecutive_count.append(counter)
            counter = 0
        next += 1
        current += 1
    consecutive_count.append(counter)
    print(consecutive_count)

    return max(consecutive_count) + 1


print(longestConsecutive([100,4,200,1,3,2]))
# print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
# print(longestConsecutive([1,2,0,1]))