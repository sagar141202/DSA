# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the function should return `true` because we can reach the last index (4) from the first index (0) by jumping through the array. Similarly, given `nums = [3,2,1,0,4]`, the function should return `false` because we cannot reach the last index from the first index.

## Approach
The algorithm uses a greedy approach to track the maximum reachable index. It iterates through the array, updating the maximum reachable index at each step. If the maximum reachable index is ever less than the current index, the function returns false. The algorithm also uses a variable to track the last position that can reach the current position.

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
            // If the current index is greater than the maxReach, return false
            if (i > maxReach) {
                return false;
            }
            // Update maxReach
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
- The key to solving this problem is to track the maximum reachable index and update it at each step.
- The algorithm uses a greedy approach to solve the problem in linear time complexity.
- The space complexity is constant, making it efficient for large inputs.