# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The problem can be formally defined as: given an array `nums` of size `n` and a target sum `S`, find the number of subsets of `nums` that sum up to `S`. For example, if `nums = [1, 1, 1, 1, 1]` and `S = 3`, the subsets that sum up to `S` are `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, and `[1, 1, 1]`, so the answer is `5`.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell represents the number of subsets that sum up to a certain value. The algorithm iterates over the array and for each element, it updates the table with the new possible sums. The final answer is stored in the cell that corresponds to the target sum.

## Complexity
- Time: O(n*sum)
- Space: O(n*sum)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findTargetSumWays(vector<int>& nums, int S) {
    int sum = 0;
    for (int num : nums) sum += num;
    if (S > sum || S < -sum) return 0;
    
    int n = nums.size();
    vector<vector<int>> dp(n + 1, vector<int>(2 * sum + 1, 0));
    dp[0][sum] = 1;
    
    for (int i = 1; i <= n; i++) {
        for (int j = -sum; j <= sum; j++) {
            if (j - nums[i - 1] >= -sum) dp[i][j + sum] += dp[i - 1][j - nums[i - 1] + sum];
            if (j + nums[i - 1] <= sum) dp[i][j + sum] += dp[i - 1][j + nums[i - 1] + sum];
        }
    }
    
    return dp[n][S + sum];
}
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], S = 3
Output: 5
Input: nums = [1], S = 1
Output: 1
```

## Key Takeaways
- The problem can be solved using dynamic programming by building a 2D table.
- The algorithm iterates over the array and for each element, it updates the table with the new possible sums.
- The final answer is stored in the cell that corresponds to the target sum.