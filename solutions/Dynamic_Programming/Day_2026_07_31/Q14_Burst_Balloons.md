# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a point value. If we burst a balloon, we get the point value of the balloon. However, after bursting a balloon, the balloons on the left and right of the burst balloon will be considered as adjacent and we can burst them in the future. The goal is to find the maximum points we can get by bursting all the balloons. The balloons are initially surrounded by two dummy balloons with point value 1.

## Approach
The problem can be solved using dynamic programming. We can create a 2D array to store the maximum points that can be obtained by bursting balloons in a given range. We then fill up the array in a bottom-up manner. The maximum points for a given range can be obtained by trying all possible balloons to burst in that range and taking the maximum.

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
        // Add dummy balloons at the beginning and end
        vector<int> newNums = {1};
        for (int num : nums) {
            newNums.push_back(num);
        }
        newNums.push_back(1);
        n = newNums.size();
        
        // Create a 2D array to store the maximum points
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Fill up the array in a bottom-up manner
        for (int len = 1; len <= n - 1; len++) {
            for (int left = 0; left <= n - len - 1; left++) {
                int right = left + len - 1;
                for (int i = left; i <= right; i++) {
                    int points = newNums[left - 1] * newNums[i] * newNums[right + 1];
                    if (i > left) {
                        points += dp[left][i - 1];
                    }
                    if (i < right) {
                        points += dp[i + 1][right];
                    }
                    dp[left][right] = max(dp[left][right], points);
                }
            }
        }
        
        return dp[1][n - 2];
    }
};
```

## Test Cases
```
Input: [3,1,5,8]
Output: 167
```

## Key Takeaways
- The problem can be solved using dynamic programming.
- We need to add dummy balloons at the beginning and end to handle the edge cases.
- The time complexity is O(n^3) due to the three nested loops.
- The space complexity is O(n^2) due to the 2D array used to store the maximum points.