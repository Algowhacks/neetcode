"""
Method: Bucket Sort
Time Complexity: O(n)
Space Complexity: O(n)

nums = [1,1,1,2,2,3]

------------------------------------
index(count) | 0 |  1  |  2  |  3  |
------------------------------------
value        |   | [3] | [2] | [1] |
------------------------------------

In the hashmap, we keep track of the number of times an element appears in the list.
The index of the hashmap is the number of occurences of the element, the values in the hashmap
is an array of those values that occur the same number of times.

As we can see, 1 appears 3 times, so the hashmap at an index same to the value we'll have all those
elements that appear the same number of times.

Let's see how this works:

"""
nums = [1,1,1,2,2,3]
k =2

class Solution:
    def topKFrequent(self, nums, k):
        count = {} # hashmap to keep track of the number of times an element appears in the list
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1 # Counts the number of times each value occurs in the list

        for n, c in count.items(): # n is the value, c is the number of times it occurs
            freq[c].append(n) # append the value to the hashmap at the index of the number of times it occurs

        res = [] # initialize the result array
        for i in range(len(freq)-1, -1, -1): # iterate from the last index of the hashmap to the first index
            for n in freq[i]: # 
                res.append(n)
                if len(res) == k:
                    return res


# test
s = Solution()
print(s.topKFrequent(nums, k))