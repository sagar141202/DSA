# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of ways to assign a plus or minus sign to each integer in the array such that the sum of the resulting integers equals the target sum. The array contains non-negative integers, and the target sum is an integer. For example, if the array is [1, 1, 1, 1, 1] and the target sum is 3, the function should return 5, because there are 5 ways to achieve this sum: -1+1+1+1+1, 1-1+1+1+1, 1+1-1+1+1, 1+1+1-1+1, 1+1+1+1-1.

## Approach
The problem can be solved using dynamic programming, where we build up a table of solutions to subproblems. We iterate over the array and for each integer, we update the table with the number of ways to achieve each possible sum. The final result is stored in the table at the index corresponding to the target sum. This approach ensures that we avoid redundant calculations and have an efficient solution.

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
        for (int num : nums) {
            sum += num;
        }
        if (target < -sum || target > sum) {
            return 0;
        }
        int n = nums.size();
        vector<vector<int>> dp(n + 1, vector<int>(2 * sum + 1, 0));
        dp[0][sum] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < 2 * sum + 1; j++) {
                if (dp[i - 1][j] > 0) {
                    if (j - nums[i - 1] >= 0) {
                        dp[i][j - nums[i - 1]] += dp[i - 1][j];
                    }
                    if (j + nums[i - 1] <= 2 * sum) {
                        dp[i][j + nums[i - 1]] += dp[i - 1][j];
                    }
                }
            }
        }
        return dp[n][sum + target];
    }
};
```

## Test Cases
```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
```

## Key Takeaways
- The problem can be solved using dynamic programming to avoid redundant calculations.
- The time complexity is O(n*sum), where n is the number of integers in the array and sum is the sum of all integers in the array.
- The space complexity is O(n*sum), which is used to store the table of solutions to subproblems.