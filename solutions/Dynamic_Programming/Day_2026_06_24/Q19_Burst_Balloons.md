# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a certain point value. If we burst a balloon, we get points equivalent to the product of the values of the balloons to the immediate left and right of it (if they exist). The goal is to find the maximum points we can get by bursting all the balloons. The input is an array of integers representing the point values of the balloons. The array is 1-indexed, and the first and last elements are always 1, representing the points for the "virtual" balloons on the left and right ends. The constraints are 1 <= n <= 500, and 0 <= nums[i] <= 10^6.

## Approach
This problem can be solved using dynamic programming by considering all possible bursts of balloons and calculating the maximum points that can be obtained. The idea is to divide the problem into smaller sub-problems and store the results of these sub-problems to avoid redundant calculations. We will use a 2D array to store the maximum points for each sub-problem.

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
        // Add 1 at the beginning and the end to represent the "virtual" balloons
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        n += 2;
        
        // Initialize a 2D array to store the maximum points for each sub-problem
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Fill the dp array in a bottom-up manner
        for (int length = 1; length < n; length++) {
            for (int left = 0; left < n - length; left++) {
                int right = left + length;
                for (int i = left; i < right; i++) {
                    // Calculate the maximum points for the current sub-problem
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]);
                }
            }
        }
        
        // The maximum points for the entire problem is stored in dp[0][n-1]
        return dp[0][n-1];
    }
};
```

## Test Cases
```
Input: [3,1,5,8]
Output: 167
```

## Key Takeaways
- Divide the problem into smaller sub-problems and store the results to avoid redundant calculations.
- Use a 2D array to store the maximum points for each sub-problem.
- Fill the dp array in a bottom-up manner to ensure that the results of smaller sub-problems are available when needed.