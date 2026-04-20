# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order. The input array will have a length of at least 2, and the absolute value of each element will be less than 10^5. The absolute value of the target will also be less than 10^5. For example, given `nums = [2, 7, 11, 15]` and `target = 9`, the output should be `[0, 1]` because `nums[0] + nums[1] = 2 + 7 = 9`.

## Approach
The approach is to use a hash table to store the numbers in the array as we iterate through it, and for each number, check if its complement (the number that would add up to the target) is already in the hash table. If it is, we return the indices of the current number and its complement. The hash table allows us to look up numbers in constant time, making the overall time complexity linear.

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
        unordered_map<int, int> numToIndex;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (numToIndex.find(complement) != numToIndex.end()) {
                return {numToIndex[complement], i};
            }
            numToIndex[nums[i]] = i;
        }
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
- Use a hash table to store the numbers and their indices for efficient lookups.
- Iterate through the array and check if the complement of each number is already in the hash table.
- Return the indices of the two numbers that add up to the target as soon as they are found.