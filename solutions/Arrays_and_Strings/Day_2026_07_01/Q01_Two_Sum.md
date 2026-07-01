# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order. For example, given `nums = [2, 7, 11, 15]` and `target = 9`, the output should be `[0, 1]` because `nums[0] + nums[1] == 2 + 7 == 9`.

## Approach
We will use a hash map to store the elements of the array as keys and their indices as values. Then, for each element, we will check if its complement (target - current element) exists in the hash map. If it does, we return the indices of the current element and its complement.

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
        // Create a hash map to store elements and their indices
        unordered_map<int, int> numToIndex;
        
        // Iterate over the array
        for (int i = 0; i < nums.size(); i++) {
            // Calculate the complement of the current element
            int complement = target - nums[i];
            
            // Check if the complement exists in the hash map
            if (numToIndex.find(complement) != numToIndex.end()) {
                // Return the indices of the current element and its complement
                return {numToIndex[complement], i};
            }
            
            // If not, add the current element to the hash map
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
```

## Key Takeaways
- Use a hash map to store elements and their indices for efficient lookups.
- Iterate over the array and check for the complement of each element in the hash map.
- Return the indices of the elements that add up to the target.