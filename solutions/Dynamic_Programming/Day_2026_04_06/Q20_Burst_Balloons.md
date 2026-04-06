# Burst Balloons

## Problem Statement
Given a list of balloons where each balloon is represented by an integer array `nums` of size `n` where `nums[i]` is the value obtained when the `i-th` balloon is burst. The goal is to find the maximum coins that can be collected by bursting the balloons in a specific order, given that when a balloon is burst, the coins collected are the product of the values of the burst balloon and its adjacent balloons. If a balloon is at the boundary, consider the value of the adjacent balloon as 1.

## Approach
The problem can be solved by using dynamic programming, where we consider each subarray of the given array and calculate the maximum coins that can be collected by bursting the balloons in that subarray. We use a 2D array `dp` to store the maximum coins for each subarray. The algorithm iterates over all possible subarrays and calculates the maximum coins by considering each balloon as the last burst balloon.

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
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        int m = nums.size();
        vector<vector<int>> dp(m, vector<int>(m, 0));

        for (int len = 1; len <= n + 1; len++) {
            for (int left = 0; left <= n && left + len - 1 < m; left++) {
                int right = left + len - 1;
                for (int i = left; i <= right; i++) {
                    int coins = nums[left - 1] * nums[i] * nums[right + 1];
                    if (left < i) coins += dp[left][i - 1];
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
Input: nums = [3,1,5,8]
Output: 167
Input: nums = [9,1,5]
Output: 52
```

## Key Takeaways
- Divide the problem into smaller subproblems and solve them using dynamic programming.
- Use a 2D array to store the maximum coins for each subarray.
- Iterate over all possible subarrays and calculate the maximum coins by considering each balloon as the last burst balloon.