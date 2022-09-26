from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        sum = 0
        for j in nums:
            if j % 2 == 0:
                sum += j

        for i in queries:
            if nums[i[1]] % 2 == 0:
                temp = nums[i[1]]
            else:
                temp = 0

            nums[i[1]] = nums[i[1]] + i[0]

            sum -= temp
            if nums[i[1]] % 2 == 0:
                sum += nums[i[1]]

            result.append(sum)
        return result

sol = Solution()

result = sol.sumEvenAfterQueries(
    [1,2,3,4],
    [[1,0],[-3,1],[-4,0],[2,3]]
)

print(result)

