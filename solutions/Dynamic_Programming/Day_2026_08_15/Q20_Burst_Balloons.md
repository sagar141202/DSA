# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it, which represents the coins you would receive when you burst the balloon. When you burst a balloon, you receive the coins printed on it, and the balloons on the left and right of the burst balloon (if they exist) will have their coins multiplied by the value of the burst balloon (1 if the burst balloon has no neighboring balloon). Find the maximum coins you can receive by bursting the balloons.

## Approach
This problem can be solved using dynamic programming, where we build up a 2D table to store the maximum coins we can get for each subproblem. The key insight is to consider the last balloon to burst in each subproblem and try all possibilities.

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
        // pad the nums with 1, to handle edge cases
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        n += 2;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int len = 1; len <= n - 1; ++len) {
            for (int left = 0; left <= n - len - 1; ++left) {
                int right = left + len - 1;
                for (int i = left; i <= right; ++i) {
                    dp[left][right] = max(dp[left][right], 
                                           (i > left ? dp[left][i - 1] : 0) +
                                           (i < right ? dp[i + 1][right] : 0) +
                                           nums[left - 1] * nums[i] * nums[right + 1]);
                }
            }
        }
        return dp[0][n - 2];
    }
};
```

## Test Cases
```
Input: [3,1,5,8]
Output: 167
```

## Key Takeaways
- Divide the problem into smaller subproblems and solve them using dynamic programming.
- Consider the last balloon to burst in each subproblem and try all possibilities.
- The time complexity can be optimized by using a more efficient algorithm or data structure.