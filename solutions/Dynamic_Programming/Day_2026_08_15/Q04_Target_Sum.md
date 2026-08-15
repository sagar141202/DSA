# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The problem can be formalized as follows: given an array `nums` and a target sum `S`, return the number of subsets that sum up to `S`. For example, if `nums = [1, 1, 1, 1, 1]` and `S = 3`, the subsets that sum up to `S` are `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, and `[1, 1, 1]`, so the output should be `5`.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the number of subsets that sum up to each possible sum. We iterate over the array and update the table accordingly. The final answer will be stored in the cell corresponding to the target sum.

## Complexity
- Time: O(n*sum)
- Space: O(n*sum)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (S > sum || S < -sum) return 0;
        int n = nums.size();
        vector<vector<int>> dp(n + 1, vector<int>(2 * sum + 1, 0));
        dp[0][sum] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = -sum; j <= sum; j++) {
                if (j - nums[i - 1] >= -sum) {
                    dp[i][j + sum] += dp[i - 1][j - nums[i - 1] + sum];
                }
                if (j + nums[i - 1] <= sum) {
                    dp[i][j + sum] += dp[i - 1][j + nums[i - 1] + sum];
                }
            }
        }
        return dp[n][S + sum];
    }
};
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], S = 3
Output: 5
```

## Key Takeaways
- The problem can be solved using dynamic programming, where we build a 2D table to store the number of subsets that sum up to each possible sum.
- The time complexity is O(n*sum), where n is the size of the array and sum is the sum of all elements in the array.
- The space complexity is O(n*sum), which is used to store the 2D table.