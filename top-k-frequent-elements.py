import numpy as np

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_object: dict = {}
        result: List[int] = []

        if len(nums) == 1:
            return nums

        for num in nums:
            if str(num) in num_object.keys():
                num_object[str(num)] += 1
            else:
                num_object[str(num)] = 1


        keys = list(num_object.keys())
        values = list(num_object.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

        new_keys = list(sorted_dict.keys())
        new_keys.reverse()

        print(new_keys)
        return [ int(new_keys[i]) for i in range(k) ]