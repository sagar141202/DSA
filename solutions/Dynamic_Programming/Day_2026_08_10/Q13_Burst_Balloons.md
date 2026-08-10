# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a certain point value. If you burst a balloon, you get the point value of that balloon plus the points from the balloons on the left and right (if they exist). The points from the left and right balloons are only added if they exist and have not been burst yet. The goal is to find the maximum points that can be obtained by bursting all the balloons. The input is an array of integers representing the point values of the balloons. The output should be the maximum points that can be obtained.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the maximum points that can be obtained by bursting balloons in a given range. We fill the table in a bottom-up manner, considering all possible ranges of balloons. The maximum points for a given range are calculated by trying all possible balloons to burst and taking the maximum.

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
        vector<int> newNums = {1};
        for (int num : nums) {
            newNums.push_back(num);
        }
        newNums.push_back(1);
        
        // Create a 2D table to store the maximum points
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        
        // Fill the table in a bottom-up manner
        for (int length = 1; length <= n + 1; length++) {
            for (int left = 0; left <= n; left++) {
                int right = left + length - 1;
                if (right > n) break;
                for (int i = left; i <= right; i++) {
                    // Calculate the maximum points for the current range
                    int coins = newNums[left - 1] * newNums[i] * newNums[right + 1];
                    if (i > left) coins += dp[left][i - 1];
                    if (i < right) coins += dp[i + 1][right];
                    dp[left][right] = max(dp[left][right], coins);
                }
            }
        }
        
        // The maximum points are stored in the last cell of the table
        return dp[1][n];
    }
};
```

## Test Cases
```
Input: [3,1,5,8]
Output: 167
```

## Key Takeaways
- The problem can be solved using dynamic programming with a time complexity of O(n^3).
- The space complexity is O(n^2) due to the 2D table used to store the maximum points.
- The solution involves filling the table in a bottom-up manner and considering all possible ranges of balloons.