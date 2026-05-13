# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a certain point value. If we burst a balloon, we get the point value of that balloon plus the point values of the balloons to the left and right if they exist. The goal is to find the maximum points that can be obtained by bursting all the balloons. The input is an array of integers representing the point values of the balloons.

## Approach
The problem can be solved using dynamic programming by iterating over all possible subarrays and calculating the maximum points that can be obtained by bursting the balloons in that subarray. The key insight is to consider the last balloon to be burst in each subarray.

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
        vector<int> balloons(n + 2);
        for (int i = 0; i < n; i++) {
            balloons[i + 1] = nums[i];
        }
        balloons[0] = 1;
        balloons[n + 1] = 1;
        
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        
        for (int length = 1; length <= n + 1; length++) {
            for (int left = 0; left <= n + 1 - length; left++) {
                int right = left + length - 1;
                for (int i = left; i <= right; i++) {
                    int coins = balloons[left - 1] * balloons[i] * balloons[right + 1];
                    if (i > left) {
                        coins += dp[left][i - 1];
                    }
                    if (i < right) {
                        coins += dp[i + 1][right];
                    }
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
- Divide the problem into smaller subproblems and store their results to avoid redundant calculations.
- Use dynamic programming to solve problems that have overlapping subproblems.
- The choice of the last balloon to be burst in each subarray is crucial in this problem.