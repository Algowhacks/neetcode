'''
128. Longest Consecutive Sequence
Medium

10286

460

Add to List

Share
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numset = set()
        for num in nums:
            numset.add(num)
        longest_streak = 1
        for i in numset:
            if i-1 in numset:
                continue
            i+=1
            current_streak = 1
            while i in numset:
                current_streak+=1
                i+=1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak
        
                
        