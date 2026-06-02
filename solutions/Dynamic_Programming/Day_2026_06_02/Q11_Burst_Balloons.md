# Burst Balloons

## Problem Statement
Given n balloons, each with a numerical value, the goal is to burst them in a way that maximizes the total score. When a balloon is burst, the score is calculated as the product of the values of the balloons to its immediate left and right. If there's no balloon to the left or right, the score is considered to be 1. The task is to find the maximum total score that can be achieved by bursting all balloons.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the maximum score for each subproblem. We iterate over all possible balloon bursts and calculate the maximum score by considering the scores of the balloons to the left and right. The algorithm uses a bottom-up approach to fill the table.

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
        // Add 1 at the beginning and end to handle edge cases
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        
        // Initialize a 2D table to store the maximum score for each subproblem
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        
        // Fill the table in a bottom-up manner
        for (int length = 1; length <= n + 1; length++) {
            for (int left = 0; left <= n + 1 - length; left++) {
                int right = left + length - 1;
                for (int i = left; i <= right; i++) {
                    // Calculate the score for the current balloon burst
                    int score = nums[left - 1] * nums[i] * nums[right + 1];
                    // Update the maximum score for the current subproblem
                    if (i > left) score += dp[left][i - 1];
                    if (i < right) score += dp[i + 1][right];
                    // Update the maximum score in the table
                    dp[left][right] = max(dp[left][right], score);
                }
            }
        }
        
        // The maximum total score is stored in the last cell of the table
        return dp[1][n];
    }
};
```

## Test Cases
```
Input: nums = [3,1,5,8]
Output: 167
```

## Key Takeaways
- The dynamic programming approach helps to avoid redundant calculations and reduces the time complexity.
- The 2D table is used to store the maximum score for each subproblem, making it easier to fill the table in a bottom-up manner.
- The algorithm handles edge cases by adding 1 at the beginning and end of the input array, ensuring that the score calculation is correct for the first and last balloons.