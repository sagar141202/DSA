# Target Sum

## Problem Statement
Given an array of integers, find the number of subsets that sum up to a target value. The array can contain both positive and negative integers. For example, given the array [1, 1, 1, 1, 1] and a target sum of 3, there are 5 subsets that sum up to 3: [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], and [1, 1, 1]. The constraints are: 1 <= array length <= 20, -10^6 <= array elements <= 10^6, and -10^6 <= target sum <= 10^6.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell represents the number of subsets that sum up to a certain value. The algorithm iterates over the array and updates the table accordingly. The final result is stored in the last cell of the table. This approach ensures that all possible subsets are considered.

## Complexity
- Time: O(n * sum)
- Space: O(n * sum)

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
        int offset = sum;
        vector<vector<int>> dp(n + 1, vector<int>(2 * sum + 1, 0));
        
        dp[0][offset] = 1;
        
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= 2 * sum; j++) {
                if (j - nums[i - 1] >= 0) dp[i][j] += dp[i - 1][j - nums[i - 1]];
                if (j + nums[i - 1] <= 2 * sum) dp[i][j] += dp[i - 1][j + nums[i - 1]];
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
```

## Key Takeaways
- The dynamic programming approach is suitable for this problem because it allows us to break down the problem into smaller subproblems and store the results in a table for later use.
- The 2D table is used to store the number of subsets that sum up to a certain value, and the final result is stored in the last cell of the table.
- The time complexity is O(n * sum) because we iterate over the array and the table, and the space complexity is O(n * sum) because we need to store the table.