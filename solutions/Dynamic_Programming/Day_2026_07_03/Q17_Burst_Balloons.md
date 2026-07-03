# Burst Balloons

## Problem Statement
Given a list of integers representing the coins that can be obtained by bursting a balloon, find the maximum coins that can be collected. The list is circular, meaning the first and last elements are considered adjacent. When a balloon is burst, the coins obtained are the product of the coins of the left and right adjacent balloons plus the coins of the current balloon. The goal is to find the maximum coins that can be collected by bursting all the balloons.

## Approach
The problem can be solved using dynamic programming by considering all possible balloon burst orders and calculating the maximum coins that can be collected. The algorithm uses a 2D array to store the maximum coins that can be collected for each subproblem. The final result is the maximum coins that can be collected for the entire list.

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
        // Add 1 at the beginning and the end to handle edge cases
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        n += 2;
        
        // Create a 2D array to store the maximum coins that can be collected for each subproblem
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Fill the dp array in a bottom-up manner
        for (int len = 1; len < n; len++) {
            for (int left = 0; left < n - len; left++) {
                int right = left + len;
                for (int i = left + 1; i < right; i++) {
                    // Calculate the maximum coins that can be collected by bursting the current balloon
                    dp[left][right] = max(dp[left][right], dp[left][i] + dp[i][right] + nums[left] * nums[i] * nums[right]);
                }
            }
        }
        
        // The final result is the maximum coins that can be collected for the entire list
        return dp[0][n - 1];
    }
};
```

## Test Cases
```
Input: [3,1,5,8]
Output: 167
```

## Key Takeaways
- The problem can be solved using dynamic programming by considering all possible balloon burst orders.
- The algorithm uses a 2D array to store the maximum coins that can be collected for each subproblem.
- The final result is the maximum coins that can be collected for the entire list.