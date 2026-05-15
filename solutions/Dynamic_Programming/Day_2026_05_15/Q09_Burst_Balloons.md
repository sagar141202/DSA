# Burst Balloons

## Problem Statement
Given n balloons, each with a number of coins associated with it. When a balloon is burst, the coins associated with it and its adjacent balloons are added to the total coins. The goal is to find the maximum number of coins that can be collected by bursting the balloons in a specific order. The balloons are numbered from 0 to n-1, and the coins associated with each balloon are given in an array nums. The balloons are initially surrounded by two dummy balloons with 1 coin each.

## Approach
The problem can be solved using dynamic programming by considering each balloon as a potential last balloon to be burst and calculating the maximum coins that can be collected. The algorithm uses a 2D array to store the maximum coins that can be collected for each subproblem. The final result is the maximum coins that can be collected for the entire array.

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
        // add dummy balloons
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        
        for (int len = 1; len <= n + 1; len++) {
            for (int left = 0; left <= n; left++) {
                int right = left + len - 1;
                if (right > n) break;
                
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
- The problem can be solved using dynamic programming by considering each balloon as a potential last balloon to be burst.
- The algorithm uses a 2D array to store the maximum coins that can be collected for each subproblem.
- The time complexity of the algorithm is O(n^3) and the space complexity is O(n^2).