# https://leetcode.com/problems/contains-duplicate-ii/
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        batch = []
        batch_set = set()
        for i, n in enumerate(nums):
            if not batch:
                batch = nums[i:k+1+i]
                batch_set = set(batch)
            else:
                batch_set.remove(batch[0])
                batch.pop(0)
                if i+k < len(nums):
                    batch.append(nums[i+k])
                    batch_set.add(nums[i+k])
                else:
                    break
            if len(batch_set) != len(batch):
                return True
        return False


print(Solution().containsNearbyDuplicate(nums=[1,0,1,1], k=1))  # True
print(Solution().containsNearbyDuplicate(nums=[1,2,3,1], k=3))  # True
print(Solution().containsNearbyDuplicate(nums=[1,2,3,1,2,3], k=2))  # False