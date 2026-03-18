# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. For example, given the array `[1, 1, 1, 1, 1]` and a target sum of `3`, the subsets that sum up to `3` are `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, and `[1, 1, 1]`, so the answer is `5`. The array can have up to `20` elements and the target sum can range from `-1000` to `1000`.

## Approach
We will use dynamic programming to solve this problem, where we build up a table of solutions to subproblems. The table will store the number of subsets that sum up to each possible total from `-1000` to `1000`. We will iterate over the array and for each element, we will update the table with the new number of subsets that sum up to each possible total.

## Complexity
- Time: O(n * sum)
- Space: O(sum)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (target > sum || target < -sum) {
            return 0;
        }
        int offset = sum;
        vector<vector<int>> dp(nums.size() + 1, vector<int>(2 * sum + 1, 0));
        dp[0][offset] = 1;
        for (int i = 1; i <= nums.size(); i++) {
            for (int j = 0; j <= 2 * sum; j++) {
                if (j - nums[i - 1] >= 0 && j - nums[i - 1] <= 2 * sum) {
                    dp[i][j] += dp[i - 1][j - nums[i - 1]];
                }
                if (j + nums[i - 1] >= 0 && j + nums[i - 1] <= 2 * sum) {
                    dp[i][j] += dp[i - 1][j + nums[i - 1]];
                }
            }
        }
        return dp[nums.size()][offset + target];
    }
};
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5
```

## Key Takeaways
- Use dynamic programming to build up a table of solutions to subproblems.
- The table should store the number of subsets that sum up to each possible total.
- Iterate over the array and update the table with the new number of subsets that sum up to each possible total.