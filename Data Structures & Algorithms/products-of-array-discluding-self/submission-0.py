class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = n*[1]
        prefix = 1
        sufix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        for i in range(n-1, -1, -1):
            output[i] *= sufix
            sufix *= nums[i]

        return output
        