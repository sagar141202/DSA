# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it, represented by an array nums. You have a function to burst a balloon, which will make the balloon disappear and return the coins that you get. If the balloon that you burst has a number x on it, you will get x * (number to the left) * (number to the right) coins. If there is no balloon to the left, you get x * 1 * (number to the right) coins. If there is no balloon to the right, you get x * (number to the left) * 1 coins. Find the maximum coins you can get.

## Approach
The problem can be solved using dynamic programming by considering each balloon as a potential last balloon to burst and calculating the maximum coins that can be obtained. The algorithm involves iterating over all possible last balloons and using a 2D DP table to store the maximum coins for each subproblem.

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
        // Add 1 at the beginning and the end of nums
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        n += 2;
        
        // Initialize a 2D DP table
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Fill the DP table in a bottom-up manner
        for (int length = 1; length < n; length++) {
            for (int left = 0; left < n - length; left++) {
                int right = left + length;
                for (int i = left + 1; i < right; i++) {
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]);
                }
            }
        }
        
        // The maximum coins can be obtained by bursting the last balloon
        return dp[0][n - 1];
    }
};
```

## Test Cases
```
Input: nums = [3,1,5,8]
Output: 167
```

## Key Takeaways
- The problem can be solved using dynamic programming by considering each balloon as a potential last balloon to burst.
- The algorithm involves iterating over all possible last balloons and using a 2D DP table to store the maximum coins for each subproblem.
- The maximum coins can be obtained by bursting the last balloon and considering the maximum coins that can be obtained by bursting the remaining balloons.