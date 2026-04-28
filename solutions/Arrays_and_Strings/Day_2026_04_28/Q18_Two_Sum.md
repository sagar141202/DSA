# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order. For example, given `nums = [2, 7, 11, 15]` and `target = 9`, return `[0, 1]` because `nums[0] + nums[1] == 2 + 7 == 9`.

## Approach
We will use a hash table to store the elements of the array as we iterate through it, keeping track of the index of each element. This allows us to check in constant time if the complement of the current element (i.e., the value needed to reach the target) is in the hash table.

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
        
        // Iterate through the array
        for (int i = 0; i < nums.size(); i++) {
            // Calculate the complement of the current element
            int complement = target - nums[i];
            
            // Check if the complement is in the hash table
            if (hashTable.find(complement) != hashTable.end()) {
                // Return the indices of the current element and its complement
                return {hashTable[complement], i};
            }
            
            // Add the current element to the hash table
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
```

## Key Takeaways
- Using a hash table allows us to solve the problem in linear time complexity.
- We only need to iterate through the array once to find the solution.
- The hash table stores the elements and their indices, allowing us to look up the complement of an element in constant time.