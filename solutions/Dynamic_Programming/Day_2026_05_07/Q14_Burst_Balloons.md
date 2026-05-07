# Burst Balloons

## Problem Statement
Given a list of balloons where each balloon is represented by an array of two integers, the first integer representing the start index of the balloon and the second integer representing the end index of the balloon. The task is to find the maximum coins that can be collected by bursting the balloons. When a balloon is burst, the coins collected are equal to the product of the start index and the end index of the balloon plus the coins collected by bursting the remaining balloons.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the maximum coins that can be collected for each subproblem. We iterate over the table and for each cell, we calculate the maximum coins that can be collected by bursting the balloon at the current position.

## Complexity
- Time: O(n^4)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<int> new_nums = {1};
        for (int num : nums) {
            new_nums.push_back(num);
        }
        new_nums.push_back(1);
        n += 2;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int len = 1; len < n - 1; len++) {
            for (int left = 0; left < n - len - 1; left++) {
                int right = left + len + 1;
                for (int i = left + 1; i < right; i++) {
                    dp[left][right] = max(dp[left][right], new_nums[left] * new_nums[i] * new_nums[right] + dp[left][i] + dp[i][right]);
                }
            }
        }
        
        return dp[0][n - 1];
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
- The problem requires a dynamic programming approach to solve it efficiently.
- The 2D table `dp` is used to store the maximum coins that can be collected for each subproblem.
- The time complexity of the solution is O(n^4) due to the four nested loops.