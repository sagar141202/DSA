# Burst Balloons

## Problem Statement
Given n balloons, each with a numerical value, the goal is to burst them in a way that maximizes the total score. When a balloon is burst, the score is calculated as the product of the values of the balloons to its immediate left and right. If there is no balloon to the left or right, the score is considered to be 1. The problem requires finding the maximum total score that can be achieved by bursting all the balloons.

## Approach
The problem can be solved using dynamic programming by iterating over all possible subsets of balloons and calculating the maximum score for each subset. The maximum score for a subset is calculated by considering each balloon in the subset as the last balloon to be burst and calculating the score accordingly.

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
        // Add 1 at the beginning and end to handle edge cases
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        n += 2;
        
        // Initialize dp table
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Fill dp table in a bottom-up manner
        for (int len = 1; len < n; len++) {
            for (int left = 0; left < n - len; left++) {
                int right = left + len;
                for (int i = left; i < right; i++) {
                    // Calculate the score for the current balloon
                    int score = nums[left - 1] * nums[i] * nums[right] + dp[left][i] + dp[i + 1][right];
                    // Update the maximum score
                    dp[left][right] = max(dp[left][right], score);
                }
            }
        }
        
        // The maximum total score is stored in dp[1][n - 1]
        return dp[1][n - 1];
    }
};
```

## Test Cases
```
Input: nums = [3,1,5,8]
Output: 167
```

## Key Takeaways
- The problem requires using dynamic programming to calculate the maximum score for each subset of balloons.
- The dp table is filled in a bottom-up manner by considering each possible subset of balloons.
- The maximum total score is stored in the dp table and can be retrieved after filling the table.