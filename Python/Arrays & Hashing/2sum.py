"""
2 sum leetcode question

To solve this problem we can loop over an array and use
a dictionary to keep track the values that we want to see.

For example, for an element x in our array, and a target value,
we want to see if there's another elemet in the array that has  a 
the value of target - x (called the compliment)

We can use a dict to keep track of values and indices of values 
we have seen so far. Map the value of an element to the corresponding index position

For each element we want to compute the complement(target-element) 
we check if the complement
of an element is in a dict, if yes, we return the current index of the 
element and the value of 
the compliment in the array to get the indices of the two elements that
add up to the target value.
if not, we map the element to the index position in the array.

if no 2 elements add up to the target value, we return an empty list.
"""

nums = [2,     11,      15,  7]

target = 9

# complement = target - element

# value | index
# ----------------
# 2    | 0
# 11   | 1
# 15   | 2

class Solution:
    def twoSum(self, nums, target):
        
        seen = {}

        for i, num in enumerate(nums): # i is the index, num is the value
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []


# test solution
s = Solution()
print(s.twoSum(nums, target))

# time complexity: O(n) - we loop over the array once to get the complement
# space complexity: O(n) - we use a dictionary to keep track of values and indices