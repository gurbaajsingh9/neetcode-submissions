class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}
        output = []
        for i in range(len(nums)):
            if target - nums[i] not in sum:
                sum [nums[i]] = i
            else:
                output.append(sum[target - nums[i]])
                output.append(i)
        return output