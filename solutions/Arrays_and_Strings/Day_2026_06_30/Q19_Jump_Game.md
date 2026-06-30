# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the function should return `true` because we can reach the last index (4) from the first index (0) by jumping 1 step from index 0 to index 1, then 3 steps to index 4. On the other hand, given `nums = [3,2,1,0,4]`, the function should return `false` because we cannot reach the last index from the first index.

## Approach
The approach to solve this problem is to use a greedy algorithm, keeping track of the maximum reachable position from the start. We initialize the maximum reachable position to 0 and then iterate over the array, updating the maximum reachable position at each step.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.size(); i++) {
            // If we cannot reach this position, return false
            if (i > maxReach) {
                return false;
            }
            // Update the maximum reachable position
            maxReach = max(maxReach, i + nums[i]);
        }
        return true;
    }
};
```

## Test Cases
```
Input: nums = [2,3,1,1,4]
Output: true
Input: nums = [3,2,1,0,4]
Output: false
```

## Key Takeaways
- We use a greedy algorithm to solve this problem because we only need to keep track of the maximum reachable position.
- The time complexity is O(n) because we only iterate over the array once.
- The space complexity is O(1) because we only use a constant amount of space to store the maximum reachable position.