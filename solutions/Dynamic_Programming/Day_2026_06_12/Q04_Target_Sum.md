# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The problem can be formalized as follows: given an array `nums` and an integer `target`, return the number of subsets that sum up to `target`. The array can contain duplicate elements, and each element can be used only once in a subset.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the number of subsets that sum up to each possible total. We iterate over the array and for each element, we update the table with the number of subsets that sum up to the current total with and without the current element. The final answer will be stored in the cell corresponding to the target sum.

## Complexity
- Time: O(n*sum), where n is the number of elements in the array and sum is the maximum possible sum.
- Space: O(n*sum), for the 2D table.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
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
                if (j - nums[i - 1] >= 0 && j - nums[i - 1] <= 2 * sum) {
                    dp[i][j] += dp[i - 1][j - nums[i - 1]];
                }
                if (j + nums[i - 1] >= 0 && j + nums[i - 1] <= 2 * sum) {
                    dp[i][j] += dp[i - 1][j + nums[i - 1]];
                }
            }
        }
        return dp[n][offset + target];
    }
};
```

## Test Cases
```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Input: nums = [1], target = 1
Output: 1
```

## Key Takeaways
- The problem can be solved using dynamic programming with a time complexity of O(n*sum) and a space complexity of O(n*sum).
- The 2D table is used to store the number of subsets that sum up to each possible total.
- The final answer is stored in the cell corresponding to the target sum.