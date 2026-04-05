# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the function should return `true` because we can reach the last index (4) from the first index (0) by jumping 1 step from index 0 to index 1, then 3 steps to index 4. On the other hand, given `nums = [3,2,1,0,4]`, the function should return `false` because we cannot reach the last index from the first index.

## Approach
The algorithm uses a greedy approach, maintaining the maximum reachable position as we iterate through the array. If we can reach the current position, we update the maximum reachable position. If we cannot reach the current position, we return false. The intuition is to always try to extend the maximum reachable position.

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
            // If we cannot reach the current position, return false
            if (i > maxReach) {
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
- We use a greedy approach to solve this problem.
- The maximum reachable position is updated at each step.
- If we cannot reach the current position, we immediately return false.