# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The problem can be formalized as follows: given an array `arr` of size `n` and a target sum `target`, find the number of subsets of `arr` that sum up to `target`. For example, if `arr = [1, 1, 1, 1, 1]` and `target = 3`, the subsets that sum up to `target` are `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, and `[1, 1, 1]`, so the answer is 5.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the number of subsets that sum up to each possible sum from 0 to the target sum. We iterate over the array and for each element, we update the table by adding the number of subsets that sum up to the current sum minus the current element. The final answer will be stored in the last cell of the table.

## Complexity
- Time: O(n*target)
- Space: O(n*target)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findTargetSumWays(vector<int>& nums, int target) {
    int n = nums.size();
    int sum = 0;
    for (int num : nums) {
        sum += num;
    }
    if (target > sum || target < -sum) {
        return 0;
    }
    int offset = sum;
    vector<vector<int>> dp(n + 1, vector<int>(2 * sum + 1, 0));
    dp[0][offset] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= 2 * sum; j++) {
            if (j - nums[i - 1] >= 0) {
                dp[i][j] += dp[i - 1][j - nums[i - 1]];
            }
            if (j + nums[i - 1] <= 2 * sum) {
                dp[i][j] += dp[i - 1][j + nums[i - 1]];
            }
        }
    }
    return dp[n][offset + target];
}
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5
Input: nums = [1], target = 1
Output: 1
```

## Key Takeaways
- The problem can be reduced to a subset sum problem with a target sum.
- Dynamic programming can be used to solve the problem efficiently by building a 2D table to store the number of subsets that sum up to each possible sum.
- The final answer will be stored in the last cell of the table.