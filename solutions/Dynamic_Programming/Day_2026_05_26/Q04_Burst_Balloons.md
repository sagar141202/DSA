# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a number of coins associated with it that you will get if you burst the balloon. If the balloon at index i is burst, you will get coins[i-1] * coins[i] * coins[i+1] coins. If i - 1 or i + 1 goes out of bounds, it is considered as if there is a balloon with 1 coin. The goal is to find the maximum number of coins that can be collected by bursting the balloons.

## Approach
The problem can be solved using dynamic programming by considering all possible subsets of balloons and calculating the maximum coins that can be collected. We use a 2D DP array where dp[i][j] represents the maximum coins that can be collected by bursting the balloons from index i to j.

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
        vector<int> coins = {1};
        for (int num : nums) coins.push_back(num);
        coins.push_back(1);
        
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        
        for (int length = 1; length <= n + 1; length++) {
            for (int left = 0; left <= n + 1 - length; left++) {
                int right = left + length - 1;
                for (int i = left; i <= right; i++) {
                    dp[left][right] = max(dp[left][right], coins[left - 1] * coins[i] * coins[right + 1] + dp[left][i - 1] + dp[i + 1][right]);
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
- Divide the problem into smaller subproblems and use dynamic programming to store and reuse the results of these subproblems.
- The state of the DP array dp[i][j] represents the maximum coins that can be collected by bursting the balloons from index i to j.
- The transition of the DP array is based on the choice of the balloon to be burst, which is the balloon that gives the maximum coins.