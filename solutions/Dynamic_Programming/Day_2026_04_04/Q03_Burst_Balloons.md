# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a certain point value, and after bursting a balloon, the point values of the balloons to the left and right of the burst balloon will change. If the balloon to the left of the burst balloon is still intact, then the point value of the balloon to the left will be multiplied by the point value of the burst balloon. Similarly, if the balloon to the right of the burst balloon is still intact, then the point value of the balloon to the right will be multiplied by the point value of the burst balloon. The goal is to find the maximum points that can be obtained by bursting all the balloons.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array to store the maximum points that can be obtained by bursting balloons in a given range. The algorithm fills up the 2D array in a bottom-up manner, considering all possible burst orders.

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
        for (int i = 1; i <= n; i++) {
            val[i] = nums[i - 1];
        }
        val[0] = 1;
        val[n + 1] = 1;

        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        for (int len = 1; len <= n + 1; len++) {
            for (int left = 0; left <= n + 1 - len; left++) {
                int right = left + len - 1;
                for (int i = left; i <= right; i++) {
                    dp[left][right] = max(dp[left][right], val[left] * val[i] * val[right + 1] + dp[left][i - 1] + dp[i + 1][right]);
                }
            }
        }
        return dp[0][n + 1];
    }
};
```

## Test Cases
```
Input: [3,1,5,8]
Output: 167
```

## Key Takeaways
- The problem requires a dynamic programming approach to consider all possible burst orders.
- The time complexity is O(n^3) due to the three nested loops.
- The space complexity is O(n^2) for storing the 2D array.