"""
Date: - 01-08-2020
Author: - SUSHIL SINGH
Problem : - Two Sum
Question- Link: - https://leetcode.com/problems/two-sum/submissions/

Time Complexity: O(n) 
Space Complexity: O(n)
"""

# code
def twoSum(nums: List[int], target: int) -> List[int]:
  table = {}

  for (i,num) in enumerate(nums):
    if (target - num) in table:
      return [nums.index(target - num), i]
    else:
      table[num] = True
    
    return []
 
