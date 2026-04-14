# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a point value when burst. You can burst the balloons from left to right, and for each balloon you burst, you get the point value of that balloon plus the product of the point values of the balloons to the left and right of it (if they exist). The goal is to find the maximum points that can be obtained by bursting all the balloons. The input is a list of integers representing the point values of the balloons. The constraints are 1 <= n <= 500, and 0 <= point values <= 100.

## Approach
The algorithm uses dynamic programming to store the maximum points that can be obtained for each subarray of balloons. The intuition is to try bursting each balloon in the subarray and take the maximum points that can be obtained. The function will use a 2D array to store the maximum points for each subarray.

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
        // add 1 at the beginning and the end to handle edge cases
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        n += 2;
        
        // create a 2D array to store the maximum points for each subarray
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // try all possible subarrays
        for (int len = 1; len <= n - 1; len++) {
            for (int left = 0; left <= n - len; left++) {
                int right = left + len - 1;
                // try bursting each balloon in the subarray
                for (int i = left; i <= right; i++) {
                    // calculate the points for bursting the current balloon
                    int points = nums[left - 1] * nums[i] * nums[right + 1];
                    // add the points for the left and right subarrays
                    if (i > left) points += dp[left][i - 1];
                    if (i < right) points += dp[i + 1][right];
                    // update the maximum points for the subarray
                    dp[left][right] = max(dp[left][right], points);
                }
            }
        }
        
        // return the maximum points for the whole array
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
- The dynamic programming approach is useful for solving problems with overlapping subproblems.
- The time complexity can be high for this problem due to the need to try all possible subarrays and bursting each balloon in the subarray.
- The space complexity is relatively low since we only need to store the maximum points for each subarray.