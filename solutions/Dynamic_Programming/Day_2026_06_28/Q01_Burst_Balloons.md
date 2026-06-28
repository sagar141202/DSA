# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a point value when burst. You can burst a balloon and get the point value, but after bursting a balloon, the balloons on the left and right will be considered adjacent and you will get the points from the new adjacent balloons. Find the maximum points you can get by bursting all the balloons. The point value of each balloon is given by the array `nums`, where `nums[i]` is the point value of the `i-th` balloon. The balloons are initially surrounded by two dummy balloons with point value 1.

## Approach
The problem can be solved using dynamic programming. The idea is to maintain a 2D array `dp` where `dp[i][j]` represents the maximum points that can be obtained by bursting the balloons from index `i` to `j`. We can fill up the `dp` array by considering all possible last balloons to burst.

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
        vector<int> newNums = {1};
        for (int num : nums) {
            newNums.push_back(num);
        }
        newNums.push_back(1);
        n += 2;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int len = 1; len < n - 1; len++) {
            for (int left = 0; left < n - len - 1; left++) {
                int right = left + len + 1;
                for (int i = left + 1; i < right; i++) {
                    dp[left][right] = max(dp[left][right], newNums[left] * newNums[i] * newNums[right] + dp[left][i] + dp[i][right]);
                }
            }
        }
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
- The problem can be solved using dynamic programming by maintaining a 2D array `dp` to store the maximum points that can be obtained by bursting the balloons from index `i` to `j`.
- The `dp` array can be filled up by considering all possible last balloons to burst.
- The time complexity of the solution is O(n^3) and the space complexity is O(n^2).