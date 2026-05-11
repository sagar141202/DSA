# House Robber

## Problem Statement
The House Robber problem is a classic dynamic programming problem where you are given a list of non-negative integers representing the amount of money in each house. The goal is to find the maximum amount of money that can be stolen from the houses without stealing from adjacent houses. The problem has the following constraints: each house can only be robbed once, and if a house is robbed, the adjacent houses cannot be robbed.

## Approach
The algorithm uses dynamic programming to build up a solution by considering each house and deciding whether to rob it or not. The decision is based on the maximum amount of money that can be stolen up to the current house. The approach involves iterating through the list of houses and at each step, considering the maximum amount of money that can be stolen by either robbing the current house or not robbing it.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        if (nums.size() == 1) {
            return nums[0];
        }
        vector<int> dp(nums.size());
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size(); i++) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        return dp[nums.size() - 1];
    }
};
```

## Test Cases
```
Input: [1,2,3,1]
Output: 4
Input: [2,7,9,3,1]
Output: 12
```

## Key Takeaways
- The problem can be solved using a bottom-up dynamic programming approach.
- The time complexity is linear, making it efficient for large inputs.
- The space complexity can be optimized to O(1) by only keeping track of the previous two houses.