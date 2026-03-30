# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order. For example, given `nums = [2, 7, 11, 15]` and `target = 9`, the output should be `[0, 1]` because `nums[0] + nums[1] == 2 + 7 == 9`.

## Approach
The approach to solve this problem is to use a hash table to store the elements of the array as keys and their indices as values. Then, for each element, we check if the difference between the target and the current element exists in the hash table. If it does, we return the indices of the current element and the difference.

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
        // Create a hash table to store the elements and their indices
        unordered_map<int, int> hashTable;
        
        // Iterate over the array
        for (int i = 0; i < nums.size(); i++) {
            // Calculate the difference between the target and the current element
            int diff = target - nums[i];
            
            // Check if the difference exists in the hash table
            if (hashTable.find(diff) != hashTable.end()) {
                // Return the indices of the current element and the difference
                return {hashTable[diff], i};
            }
            
            // If the difference does not exist, add the current element to the hash table
            hashTable[nums[i]] = i;
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
- Use a hash table to store the elements and their indices for efficient lookup.
- Iterate over the array and check if the difference between the target and the current element exists in the hash table.
- If the difference exists, return the indices of the current element and the difference.