from typing import List
import ast

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        en = len(nums) - 1
        while st <= en:
            mid = int((st + en) / 2)
            if(nums[mid] > target):
                en = mid - 1
            else:
                st = mid + 1
        if(nums[en] == target):
            return en
        else:
            return -1

sl = Solution()

# for list input
# <list> = ast.literal_eval(<string>)

with open('input.txt', 'r') as f:
    lines = ''.join(f.readlines()).split()
    count = 2
    for i in range(0, len(lines), count):
        print(sl.search(ast.literal_eval(lines[i + 0]), int(lines[i + 1])))