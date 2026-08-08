# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. For example, given the array `[1, 1, 1, 1, 1]` and a target sum of `3`, there are `5` subsets that sum up to `3`: `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, and `[1, 1, 1]`. The function should return the count of such subsets.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the number of subsets that sum up to each possible sum. We iterate over the array and update the table accordingly. The final result is stored in the table at the index corresponding to the target sum.

## Complexity
- Time: O(n*sum)
- Space: O(n*sum)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        int sum = 0;
        for (int num : nums) sum += num;
        
        // If the target sum is greater than the total sum or less than the negative of the total sum, return 0
        if (abs(target) > sum) return 0;
        
        // Create a 2D table to store the number of subsets that sum up to each possible sum
        int dp[n][2*sum + 1] = {};
        dp[0][nums[0] + sum] = 1;
        dp[0][-nums[0] + sum] = 1;
        
        // Iterate over the array and update the table accordingly
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < 2*sum + 1; j++) {
                if (dp[i-1][j] > 0) {
                    if (j - nums[i] >= 0) dp[i][j - nums[i]] += dp[i-1][j];
                    if (j + nums[i] < 2*sum + 1) dp[i][j + nums[i]] += dp[i-1][j];
                }
            }
        }
        
        // The final result is stored in the table at the index corresponding to the target sum
        return dp[n-1][target + sum];
    }
};
```

## Test Cases
```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The problem can be broken down into smaller subproblems and solved recursively, with the results stored in a table to avoid redundant computation.
- The time complexity of the solution is O(n*sum), where n is the size of the input array and sum is the total sum of the array elements.