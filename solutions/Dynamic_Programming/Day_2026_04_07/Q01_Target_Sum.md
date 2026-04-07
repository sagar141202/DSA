# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. For example, if the array is [1, 1, 1, 1, 1] and the target sum is 3, the subsets that sum up to 3 are [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], and [1, 1, 1], so the answer is 5.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the number of subsets that sum up to each possible sum. We iterate over the array and for each element, we update the table with the number of subsets that sum up to the current sum with and without the current element.

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
        int sum = 0;
        for (int num : nums) sum += num;
        if (target > sum || target < -sum) return 0;
        
        int n = nums.size();
        int dp[n + 1][2 * sum + 1];
        memset(dp, 0, sizeof(dp));
        dp[0][sum] = 1;
        
        for (int i = 1; i <= n; i++) {
            for (int j = -sum; j <= sum; j++) {
                if (j - nums[i - 1] >= -sum) dp[i][j + sum] += dp[i - 1][j - nums[i - 1] + sum];
                if (j + nums[i - 1] <= sum) dp[i][j + sum] += dp[i - 1][j + nums[i - 1] + sum];
            }
        }
        
        return dp[n][target + sum];
    }
};
```

## Test Cases
```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
```

## Key Takeaways
- The problem can be solved using dynamic programming with a time complexity of O(n*sum) and space complexity of O(n*sum).
- The dp table is used to store the number of subsets that sum up to each possible sum.
- The base case is when the sum is equal to the target sum, in which case the number of subsets is 1.