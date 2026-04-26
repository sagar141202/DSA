# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a certain point value. When a balloon is burst, all the balloons to its left and right that have not been burst yet will have their point values added to the total score. The goal is to find the maximum total score that can be achieved by bursting the balloons in a specific order. The input is an array of integers representing the point values of the balloons. The output should be the maximum total score.

## Approach
This problem can be solved using dynamic programming, where we build a 2D table to store the maximum score for each subproblem. We iterate over all possible subarrays and calculate the maximum score by considering each balloon as the last one to be burst. The maximum score is then calculated by adding the score of the current balloon to the maximum score of the subproblems to its left and right.

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
        vector<int> values(n + 2);
        for (int i = 0; i < n; i++) {
            values[i + 1] = nums[i];
        }
        values[0] = 1;
        values[n + 1] = 1;
        
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        
        for (int length = 1; length <= n + 1; length++) {
            for (int left = 0; left <= n + 1 - length; left++) {
                int right = left + length - 1;
                for (int i = left; i <= right; i++) {
                    dp[left][right] = max(dp[left][right], values[left - 1] * values[i] * values[right + 1] + dp[left][i - 1] + dp[i + 1][right]);
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
- Dynamic programming is used to solve this problem by building a 2D table to store the maximum score for each subproblem.
- The maximum score is calculated by considering each balloon as the last one to be burst and adding its score to the maximum score of the subproblems to its left and right.
- The time complexity is O(n^3) due to the three nested loops, and the space complexity is O(n^2) for the 2D table.