# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The solution should be able to handle large inputs and provide the result modulo `10^9 + 7` to avoid overflow. For example, if `nums = [1, 2, 3]` and `target = 4`, the possible combinations are `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 3]`, and `[2, 2]`, so the result is `4`.

## Approach
This problem can be solved using dynamic programming by building up a table where each cell represents the number of combinations that sum up to the corresponding index. The algorithm iterates over the table and for each cell, it adds the number of combinations that can be formed by including the current number from `nums`. The final result is stored in the last cell of the table.

## Complexity
- Time: O(n*target)
- Space: O(target)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<unsigned int> dp(target + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= target; i++) {
            for (int num : nums) {
                if (i - num >= 0) {
                    dp[i] = (dp[i] + dp[i - num]) % (1000000007);
                }
            }
        }
        return dp[target];
    }
};
```

## Test Cases
```
Input: nums = [1, 2, 3], target = 4
Output: 7
Input: nums = [9], target = 3
Output: 0
```

## Key Takeaways
- Use dynamic programming to build up a table where each cell represents the number of combinations that sum up to the corresponding index.
- Iterate over the table and for each cell, add the number of combinations that can be formed by including the current number from `nums`.
- Use modulo operation to avoid overflow for large inputs.