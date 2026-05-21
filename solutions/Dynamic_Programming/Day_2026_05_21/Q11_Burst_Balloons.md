# Burst Balloons

## Problem Statement
Given n balloons, each with a number of coins associated with it, burst the balloons to maximize the total number of coins collected. When a balloon is burst, the coins associated with it are added to the total, along with the product of the coins associated with the balloons to its left and right. The balloons are numbered from 0 to n-1, and each balloon has a number of coins associated with it, given by the array nums. The goal is to find the maximum number of coins that can be collected by bursting the balloons.

## Approach
The approach to solve this problem is to use dynamic programming, where we build a 2D table to store the maximum coins that can be collected by bursting the balloons in the range [i, j]. We then fill up the table in a bottom-up manner, considering all possible balloons to burst.

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
        // Add 1 at the beginning and the end to simplify the calculation
        vector<int> balloons = {1};
        for (int num : nums) {
            balloons.push_back(num);
        }
        balloons.push_back(1);
        
        // Initialize a 2D table to store the maximum coins
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        
        // Fill up the table in a bottom-up manner
        for (int length = 1; length <= n + 1; length++) {
            for (int left = 0; left <= n + 1 - length; left++) {
                int right = left + length - 1;
                for (int i = left; i <= right; i++) {
                    // Calculate the maximum coins for the range [left, right]
                    dp[left][right] = max(dp[left][right], dp[left][i - 1] + dp[i + 1][right] + balloons[left - 1] * balloons[i] * balloons[right + 1]);
                }
            }
        }
        
        // Return the maximum coins for the range [1, n]
        return dp[1][n];
    }
};
```

## Test Cases
```
Input: nums = [3,1,5,8]
Output: 167
Input: nums = [1,5]
Output: 10
```

## Key Takeaways
- The dynamic programming approach is used to solve the problem by building a 2D table to store the maximum coins that can be collected.
- The table is filled up in a bottom-up manner, considering all possible balloons to burst.
- The maximum coins for the range [i, j] are calculated by considering all possible balloons to burst in the range [i, j].