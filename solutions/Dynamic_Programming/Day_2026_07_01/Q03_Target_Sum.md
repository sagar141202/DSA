# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The problem can be formalized as follows: Given an array `nums` of length `n` and a target sum `S`, find the number of subsets of `nums` that sum up to `S`. For example, if `nums = [1, 1, 1, 1, 1]` and `S = 3`, the subsets that sum up to `S` are `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, and `[1, 1, 1]`, so the answer is 5.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the number of subsets that sum up to each possible sum. We iterate over the array and for each element, we update the table with the number of subsets that sum up to the current sum with and without the current element. The final answer will be stored in the cell corresponding to the target sum.

## Complexity
- Time: O(n*S)
- Space: O(n*S)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int n = nums.size();
        int sum = 0;
        for (int num : nums) sum += num;
        
        // If the sum of the array is less than the target sum or the target sum is greater than the sum of the array, return 0
        if (abs(S) > sum) return 0;
        
        // If the target sum is not achievable, return 0
        if ((sum + S) % 2 == 1) return 0;
        
        int target = (sum + S) / 2;
        vector<vector<int>> dp(n + 1, vector<int>(target + 1, 0));
        
        // Base case: there is one way to get a sum of 0 with an empty array
        dp[0][0] = 1;
        
        // Fill up the dp table
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= target; j++) {
                // If the current number is greater than the current sum, we cannot include it
                if (nums[i - 1] > j) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    // We can either include or exclude the current number
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]];
                }
            }
        }
        
        return dp[n][target];
    }
};
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], S = 3
Output: 5
```

## Key Takeaways
- The problem can be solved using dynamic programming with a time complexity of O(n*S) and a space complexity of O(n*S).
- The key insight is to use a 2D table to store the number of subsets that sum up to each possible sum.
- The final answer will be stored in the cell corresponding to the target sum.