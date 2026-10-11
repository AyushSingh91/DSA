class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        condidate = None
        count = 0

        for num in nums:
            if count == 0:
                condidate = num

            if num == condidate:
                count += 1

            else:
                count -= 1
                
        return condidate

        