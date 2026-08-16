# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order. For example, given `nums = [2, 7, 11, 15]` and `target = 9`, the output should be `[0, 1]` because `nums[0] + nums[1] == 2 + 7 == 9`.

## Approach
The algorithm uses a hashmap to store the numbers we have seen so far and their indices. We iterate through the array and for each number, we check if its complement (i.e., the number that needs to be added to it to get the target) is in the hashmap. If it is, we return the indices of the current number and its complement.

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
        return {}; // should not reach here
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
- We use a hashmap to store the numbers we have seen so far and their indices to achieve O(1) lookup time.
- We iterate through the array only once, resulting in a time complexity of O(n).
- The space complexity is O(n) due to the use of the hashmap.