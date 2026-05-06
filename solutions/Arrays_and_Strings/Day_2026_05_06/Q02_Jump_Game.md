# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the function should return `true` because we can reach the last index (4) from the first index (0) by the following sequence of jumps: 0 -> 1 -> 3 -> 4. However, given `nums = [3,2,1,0,4]`, the function should return `false` because there is no sequence of jumps that can reach the last index.

## Approach
The algorithm uses a greedy approach to keep track of the maximum reachable position. It iterates through the array and updates the maximum reachable position at each step. If the maximum reachable position is ever less than the current position, it means we cannot reach the current position and the function returns `false`. The function returns `true` if we can reach the last index.

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
        // Initialize the maximum reachable position
        int maxReach = 0;
        
        // Iterate through the array
        for (int i = 0; i < nums.size(); i++) {
            // If the maximum reachable position is less than the current position, return false
            if (maxReach < i) {
                return false;
            }
            // Update the maximum reachable position
            maxReach = max(maxReach, i + nums[i]);
        }
        // If we can reach the last index, return true
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
- We use a greedy approach to solve the problem efficiently.
- The maximum reachable position is updated at each step to ensure we can reach the current position.
- If the maximum reachable position is ever less than the current position, we return `false` because we cannot reach the current position.