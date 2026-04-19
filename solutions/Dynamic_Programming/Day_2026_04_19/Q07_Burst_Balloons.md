# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a point value. You can burst a balloon and get the point value. If the balloon to the left and the right are not burst, you will get the points from the left and right balloons as well. Given an array of point values for the balloons, find the maximum points you can get by bursting the balloons.

## Approach
The problem can be solved using dynamic programming. The idea is to build a 2D table where each cell represents the maximum points that can be obtained by bursting the balloons in the corresponding range. The final answer will be stored in the cell that represents the range of all balloons.

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
        vector<int> baloons;
        baloons.push_back(1);
        for (int i = 0; i < n; i++) {
            baloons.push_back(nums[i]);
        }
        baloons.push_back(1);
        n += 2;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int len = 1; len < n - 1; len++) {
            for (int left = 0; left < n - len - 1; left++) {
                int right = left + len + 1;
                for (int i = left + 1; i < right; i++) {
                    dp[left][right] = max(dp[left][right], dp[left][i] + dp[i][right] + baloons[left] * baloons[i] * baloons[right]);
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
```

## Key Takeaways
- The problem requires a dynamic programming approach to find the maximum points by bursting the balloons.
- The time complexity is O(n^3) due to the three nested loops.
- The space complexity is O(n^2) for storing the 2D table.