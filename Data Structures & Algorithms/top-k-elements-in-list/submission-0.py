class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        result = []
        for i in nums:
            ans[i] = ans.get(i, 0) + 1

        for _ in range(k):
            max_value = max(ans, key = ans.get)
            result.append(max_value)
            ans.pop(max_value)

        return result

            
        