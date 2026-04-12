# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The constraints are: 1 <= array size <= 100, -10^5 <= array elements <= 10^5, and -10^5 <= target sum <= 10^5. For example, if the array is [1, 1, 1, 1, 1] and the target sum is 3, the output should be 5.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell represents the number of subsets that sum up to a certain value. The algorithm iterates over the array and updates the table accordingly. The final result is stored in the last cell of the table.

## Complexity
- Time: O(n*sum)
- Space: O(n*sum)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findTargetSumWays(vector<int>& nums, int target) {
    int sum = 0;
    for (int num : nums) {
        sum += num;
    }
    if (sum < abs(target)) return 0;
    if (target > sum) return 0;

    int n = nums.size();
    int dp[n + 1][2 * sum + 1] = {};

    dp[0][sum] = 1;

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

    return dp[n][sum + target];
}
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5
```

## Key Takeaways
- The problem can be solved using dynamic programming with a time complexity of O(n*sum) and a space complexity of O(n*sum).
- The solution involves building a 2D table where each cell represents the number of subsets that sum up to a certain value.
- The algorithm iterates over the array and updates the table accordingly, with the final result stored in the last cell of the table.