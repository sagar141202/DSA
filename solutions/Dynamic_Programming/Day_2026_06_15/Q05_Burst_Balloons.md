# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a certain point value. When a balloon is burst, it will get the points from the balloons on its left and right (if they exist). The goal is to find the maximum points that can be obtained by bursting all the balloons. The input is an array of integers representing the point values of the balloons. The output should be the maximum points that can be obtained.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the maximum points that can be obtained by bursting the balloons in a certain range. We fill up the table in a bottom-up manner, considering all possible ranges of balloons. The key idea is to consider the last balloon to be burst in each range and calculate the maximum points that can be obtained.

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
        vector<int> val(n + 2);
        val[0] = 1;
        val[n + 1] = 1;
        for (int i = 0; i < n; i++) {
            val[i + 1] = nums[i];
        }
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        for (int len = 1; len <= n + 1; len++) {
            for (int left = 0; left <= n + 1 - len; left++) {
                int right = left + len - 1;
                for (int i = left; i <= right; i++) {
                    dp[left][right] = max(dp[left][right], val[left - 1] * val[i] * val[right + 1] + dp[left][i - 1] + dp[i + 1][right]);
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
```

## Key Takeaways
- The problem requires considering all possible ranges of balloons and the last balloon to be burst in each range.
- Dynamic programming is used to store the maximum points that can be obtained by bursting the balloons in a certain range.
- The time complexity is O(n^3) due to the three nested loops, and the space complexity is O(n^2) due to the 2D table used to store the maximum points.