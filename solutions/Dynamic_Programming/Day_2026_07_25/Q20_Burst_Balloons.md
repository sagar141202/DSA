# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a point value. If we burst a balloon, we get the point value of the balloon plus the points from the balloons on the left and right (if they exist). The problem is to find the maximum points that can be obtained by bursting all the balloons. The input array is in the form {num1, num2, ..., numn} where numi is the point value of the ith balloon. The constraint is that 1 <= n <= 500 and 1 <= numi <= 10000.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array where dp[i][j] represents the maximum points that can be obtained by bursting the balloons from index i to j. We iterate over all possible subarrays and for each subarray, we try to burst each balloon and update the dp array accordingly.

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
        vector<int> balloons = {1};
        for (int num : nums) {
            balloons.push_back(num);
        }
        balloons.push_back(1);
        n += 2;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int len = 1; len < n - 1; len++) {
            for (int left = 0; left < n - len - 1; left++) {
                int right = left + len + 1;
                for (int i = left + 1; i < right; i++) {
                    dp[left][right] = max(dp[left][right], balloons[left] * balloons[i] * balloons[right] + dp[left][i] + dp[i][right]);
                }
            }
        }
        return dp[0][n - 1];
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
- The problem requires us to fill up a 2D dp array in a bottom-up manner.
- We need to consider all possible subarrays and for each subarray, try to burst each balloon to update the dp array.
- The final answer will be stored in dp[0][n-1].