from re import T


nums = [7,10,5,5,6,6,4,10,5,4,9,4,9,6,5,9,6,3,6,5,6,7,7,4,9,9,10,5,8,1,8,3,2,7,5,10,1,8,5,8,4,3,6,4,9,4,2,8,3,2,2,1,5,6,3,2,6,1,8,6,2,9,1,4,5,10,8,5,10,5,10,1,4,8,3,6,4,10,9,1,1,1,2,2,9,6,6,8,1,9,2,5,5,2,1,8,5,2,3,10]

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashset = set() # set() is a hash table and we keep track of the elements in the list
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num) # add the element to the hashset if it is not in the hashset

    
    
# test
s = Solution()
print(s.containsDuplicate(nums))

# Time Complexity: O(n) because we iterate through the list once
# Space Complexity: O(n) because we create a hashset of size n