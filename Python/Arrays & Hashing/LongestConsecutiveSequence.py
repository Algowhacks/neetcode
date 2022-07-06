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
        if len(nums) == 0:# Base case => If the array is empty
            return 0
        numset = set()# initialize a hashset
        for num in nums:
            numset.add(num)#add elements of the array to eliminate the duplicates
        longest_streak = 1#initialize longest steak as 1(minimum it can be if the array is not empty)
        for i in numset:#itrerate through the hashset
            if i-1 in numset:#check if number preceeding i in the number line is present in the hashset
                continue
            i+=1#else move to the next digit in the hashset
            current_streak = 1#initialize current streak as one 
            while i in numset:#if incremented i is present in the numset 
                current_streak+=1# incerement current streak by one 
                i+=1#increment i 
            longest_streak = max(longest_streak, current_streak)#gsetting the new longest streak based on the current streak
        return longest_streak
        
                
        