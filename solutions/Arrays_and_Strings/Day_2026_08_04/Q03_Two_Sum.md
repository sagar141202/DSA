# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. Each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order. The array will have a maximum of 1000 elements and the elements will be between -1000 and 1000. For example, given `nums = [2, 7, 11, 15]` and `target = 9`, the output should be `[0, 1]` because `nums[0] + nums[1] == 2 + 7 == 9`.

## Approach
The algorithm uses a hash table to store the elements of the array as keys and their indices as values. It iterates over the array, and for each element, it checks if the difference between the target and the current element exists in the hash table. If it does, it returns the indices of the current element and the element in the hash table.

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
        // Create a hash table to store elements and their indices
        unordered_map<int, int> numToIndex;
        
        // Iterate over the array
        for (int i = 0; i < nums.size(); i++) {
            // Calculate the difference between the target and the current element
            int diff = target - nums[i];
            
            // Check if the difference exists in the hash table
            if (numToIndex.find(diff) != numToIndex.end()) {
                // Return the indices of the current element and the element in the hash table
                return {numToIndex[diff], i};
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
- Use a hash table to store elements and their indices for efficient lookups.
- Iterate over the array and check if the difference between the target and the current element exists in the hash table.
- Return the indices of the current element and the element in the hash table if a solution is found.