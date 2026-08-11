class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right_element = -1
        for i in range(len(arr)-1, -1, -1):
            curr_value = arr[i]
            arr[i] = max_right_element

            if curr_value > max_right_element:
                max_right_element = curr_value

        return arr

        