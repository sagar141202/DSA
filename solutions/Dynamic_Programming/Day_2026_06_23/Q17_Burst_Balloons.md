# Burst Balloons

## Problem Statement
Given n balloons, each with a numerical value, the task is to burst them in such a way that the maximum score can be achieved. When a balloon is burst, the score is calculated as the product of the values of the balloons to the immediate left and right of the burst balloon, plus the value of the burst balloon itself. The goal is to find the maximum possible score that can be achieved by bursting all the balloons.

## Approach
This problem can be solved using dynamic programming, where we build a 2D table to store the maximum score that can be achieved by bursting the balloons in a given range. We fill the table in a bottom-up manner, considering all possible burst orders.

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
        // Add dummy balloons with value 1 at the beginning and end
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        n += 2;
        
        // Create a 2D table to store the maximum score
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Fill the table in a bottom-up manner
        for (int len = 1; len < n; len++) {
            for (int left = 0; left < n - len; left++) {
                int right = left + len;
                for (int i = left + 1; i < right; i++) {
                    // Calculate the score for the current burst order
                    int score = nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right];
                    // Update the maximum score
                    dp[left][right] = max(dp[left][right], score);
                }
            }
        }
        
        // The maximum score is stored in the cell corresponding to the entire range
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
- The problem requires considering all possible burst orders to achieve the maximum score.
- Dynamic programming is used to build a 2D table and store the maximum score for each range of balloons.
- The time complexity is O(n^3) due to the three nested loops used to fill the table.