# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. Each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order. For example, given `nums = [2, 7, 11, 15]` and `target = 9`, return `[0, 1]` because `nums[0] + nums[1] == 2 + 7 == 9`.

## Approach
We will use an unordered map to store the elements of the array as we iterate through it, with the key being the element and the value being its index. We will then check if the difference between the target and the current element exists in the map.

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
```

## Key Takeaways
- Use an unordered map to store elements and their indices for efficient lookups.
- Iterate through the array only once to achieve a time complexity of O(n).
- Check if the complement of the current element exists in the map to find the solution.