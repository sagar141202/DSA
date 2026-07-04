# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. For example, if the array is [1, 1, 1, 1, 1] and the target sum is 3, there are 5 subsets that sum up to 3: [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], and [1, 1, 1]. The constraints are that the array can have up to 20 elements and the target sum can range from -1000 to 1000.

## Approach
This problem can be solved using dynamic programming by building a 2D table where each cell represents the number of subsets that sum up to a certain value. The algorithm iterates over the array and updates the table based on whether the current element is included or excluded from the subset. The final result is stored in the cell corresponding to the target sum.

## Complexity
- Time: O(n * sum), where n is the number of elements in the array and sum is the target sum
- Space: O(n * sum), for the 2D table

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
- The problem can be solved using dynamic programming with a 2D table to store the number of subsets that sum up to each possible value.
- The algorithm iterates over the array and updates the table based on whether the current element is included or excluded from the subset.
- The final result is stored in the cell corresponding to the target sum.