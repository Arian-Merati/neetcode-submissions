class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_target_hash = {}
        for index, num in enumerate(nums):
            if num in nums_target_hash:
                first_index = nums_target_hash[num]
                second_index = index
                return [first_index, second_index]
            else:
                get_to_target = target - num  
                nums_target_hash[get_to_target] = index




        