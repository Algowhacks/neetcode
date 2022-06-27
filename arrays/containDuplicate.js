// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// Example 1:

// Input:
//  nums = [1,2,3,1]
// Output: true
// Example 2:

// Input: nums = [1,2,3,4]
// Output: false
// Example 3:

// Input:
 nums = [1,1,1,3,3,4,3,2,4,2]
// Output: true


//2 methods using hash ,wont achive constant space
var containsDuplicate = function(nums) {
    
    let isDuplicate = false , i= 0, checkMap = new Map()
   while (!isDuplicate && i < nums.length) {
       checkMap.set(nums[i],nums[i])
       console.log(checkMap)
       if (checkMap.size < i + 1) {
           isDuplicate = true
       }
       i++
   }
  return isDuplicate
};

console.log(containsDuplicate(nums));