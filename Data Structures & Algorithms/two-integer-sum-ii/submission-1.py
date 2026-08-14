class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i <= j:
            sum_of_num = numbers[i]+ numbers[j]
            if sum_of_num == target:
                return [i + 1, j + 1]
            elif sum_of_num < target:
                i += 1
            elif sum_of_num > target:
                j -= 1
        return -1