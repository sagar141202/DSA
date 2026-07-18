# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a certain point value. If we burst a balloon, we get points from the balloon and all the coins that are on the left and right of the burst balloon. If there are no balloons on the left or right, we still get a point. Find the maximum points that can be obtained by bursting all the balloons.

## Approach
The problem can be solved using dynamic programming by considering all possible balloon bursts and storing the maximum points for each subproblem. We use a 2D array to store the maximum points for each subproblem. The algorithm works by iterating over all possible balloon bursts and updating the maximum points for each subproblem.

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
        vector<int> values(n + 2);
        for (int i = 0; i < n; i++) {
            values[i + 1] = nums[i];
        }
        values[0] = 1;
        values[n + 1] = 1;

        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));

        for (int len = 1; len <= n + 1; len++) {
            for (int left = 0; left <= n + 1 - len; left++) {
                int right = left + len - 1;
                for (int i = left; i <= right; i++) {
                    int coins = values[left - 1] * values[i] * values[right + 1];
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The problem can be broken down into smaller subproblems and solved recursively.
- Memoization can be used to store the results of subproblems to avoid redundant calculations.