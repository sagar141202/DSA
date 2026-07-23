# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order. For example, given `nums = [2, 7, 11, 15]` and `target = 9`, return `[0, 1]` because `nums[0] + nums[1] == 2 + 7 == 9`.

## Approach
The approach is to use a hash table to store the elements of the array as we iterate through it, with the key being the element and the value being its index. We then check for each element if its complement (target - element) is already in the hash table.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Create an unordered map to store the elements and their indices
        unordered_map<int, int> numToIndex;
        
        // Iterate through the array
        for (int i = 0; i < nums.size(); i++) {
            // Calculate the complement of the current element
            int complement = target - nums[i];
            
            // Check if the complement is already in the hash table
            if (numToIndex.find(complement) != numToIndex.end()) {
                // If it is, return the indices of the current element and its complement
                return {numToIndex[complement], i};
            }
            
            // If not, add the current element to the hash table
            numToIndex[nums[i]] = i;
        }
        
        // If no solution is found, return an empty vector
        return {};
    }
};
```

## Test Cases
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Input: nums = [3, 3], target = 6
Output: [0, 1]
```

## Key Takeaways
- Using a hash table allows for efficient lookup of elements in O(1) time.
- The solution has a time complexity of O(n) because we only need to iterate through the array once.
- The space complexity is also O(n) because in the worst case, we need to store all elements in the hash table.