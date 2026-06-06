# Burst Balloons

## Problem Statement
Given n balloons, each with a numerical value, the goal is to burst them in a way that maximizes the total score. When a balloon is burst, the score is calculated as the product of the values of the burst balloon and its adjacent balloons (if they exist). The task is to find the maximum score that can be achieved by bursting the balloons in an optimal order, considering that the balloons are initially surrounded by two dummy balloons with a value of 1.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the maximum score for each subproblem. We iterate over the balloons and calculate the maximum score for each possible burst order. The algorithm considers all possible bursts and chooses the one that yields the highest score.

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
        // Add dummy balloons
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        n += 2;
        
        // Initialize dp table
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Fill dp table in a bottom-up manner
        for (int length = 1; length < n; length++) {
            for (int left = 0; left < n - length; left++) {
                int right = left + length;
                for (int i = left; i < right; i++) {
                    // Calculate the score for the current burst
                    int score = nums[left - 1] * nums[i] * nums[right] + dp[left][i] + dp[i + 1][right];
                    // Update the maximum score
                    dp[left][right] = max(dp[left][right], score);
                }
            }
        }
        
        // Return the maximum score for the entire array
        return dp[1][n - 1];
    }
};
```

## Test Cases
```
Input: [3,1,5,8]
Output: 167
```

## Key Takeaways
- Divide the problem into smaller subproblems and store their solutions in a table to avoid redundant calculations.
- Use a bottom-up dynamic programming approach to fill the table, considering all possible burst orders.
- The final solution is stored in the table and can be retrieved directly.