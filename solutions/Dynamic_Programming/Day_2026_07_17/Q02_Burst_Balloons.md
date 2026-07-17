# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a certain point value. When a balloon is burst, the points from the previous and next balloons are added to the points of the current balloon. The goal is to find the maximum points that can be obtained by bursting all the balloons. The balloons are initially surrounded by two dummy balloons with a point value of 1, which are also burst at the end.

## Approach
The problem can be solved using dynamic programming by considering all possible burst orders and storing the maximum points for each subproblem. The algorithm fills up a 2D table where each cell represents the maximum points for a given range of balloons. The maximum points are calculated by considering the points of the current balloon and the maximum points of the previous and next balloons.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        // Add dummy balloons
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        
        for (int length = 1; length <= n + 1; length++) {
            for (int left = 0; left <= n + 1 - length; left++) {
                int right = left + length - 1;
                for (int i = left; i <= right; i++) {
                    int coins = nums[left - 1] * nums[i] * nums[right + 1];
                    if (i > left) coins += dp[left][i - 1];
                    if (i < right) coins += dp[i + 1][right];
                    dp[left][right] = max(dp[left][right], coins);
                }
            }
        }
        
        return dp[1][n];
    }
};
```

## Test Cases
```
Input: [3,1,5,8]
Output: 167
Input: [1,5]
Output: 10
```

## Key Takeaways
- Divide the problem into smaller subproblems and store the results to avoid redundant calculations.
- Use dynamic programming to fill up a 2D table where each cell represents the maximum points for a given range of balloons.
- The maximum points are calculated by considering the points of the current balloon and the maximum points of the previous and next balloons.