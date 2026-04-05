# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order. For example, given `nums = [2, 7, 11, 15]` and `target = 9`, the output should be `[0, 1]` because `nums[0] + nums[1] == 2 + 7 == 9`.

## Approach
We can use a hash table to store the numbers we've seen so far and their indices. Then, for each number, we check if its complement (target - number) is in the hash table. If it is, we return the indices of the current number and its complement.

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
        // Create a hash table to store the numbers and their indices
        unordered_map<int, int> numToIndex;
        
        // Iterate over the array
        for (int i = 0; i < nums.size(); i++) {
            // Calculate the complement of the current number
            int complement = target - nums[i];
            
            // Check if the complement is in the hash table
            if (numToIndex.find(complement) != numToIndex.end()) {
                // Return the indices of the current number and its complement
                return {numToIndex[complement], i};
            }
            
            // Add the current number and its index to the hash table
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
- Use a hash table to store the numbers and their indices for efficient lookup.
- Iterate over the array and check if the complement of each number is in the hash table.
- Return the indices of the two numbers that add up to the target as soon as they are found.