# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order. For example, given `nums = [2, 7, 11, 15]` and `target = 9`, the output should be `[0, 1]` because `nums[0] + nums[1] == 2 + 7 == 9`.

## Approach
We will use a hash table to store the numbers we have seen so far and their indices. This allows us to check if the complement of the current number (i.e., the number that needs to be added to it to reach the target) has been seen before in constant time. If it has, we return the indices of the current number and its complement.

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
        // Create a hash table to store the numbers we have seen so far and their indices
        unordered_map<int, int> numToIndex;
        
        // Iterate over the array
        for (int i = 0; i < nums.size(); i++) {
            // Calculate the complement of the current number
            int complement = target - nums[i];
            
            // Check if the complement has been seen before
            if (numToIndex.find(complement) != numToIndex.end()) {
                // If it has, return the indices of the current number and its complement
                return {numToIndex[complement], i};
            }
            
            // If not, add the current number and its index to the hash table
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
- Use a hash table to store the numbers we have seen so far and their indices to achieve a time complexity of O(n).
- Check if the complement of the current number has been seen before to find the solution in constant time.
- Return the indices of the current number and its complement if the complement has been seen before.