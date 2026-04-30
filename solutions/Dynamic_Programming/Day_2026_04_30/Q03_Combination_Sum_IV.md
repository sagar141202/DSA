# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The order of the numbers in the combination does not matter. For example, if `nums = [1, 2, 3]` and `target = 4`, the combinations are `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 3]`, and `[2, 2]`, so the output is `4`.

## Approach
The problem can be solved using dynamic programming by building up a table where each cell represents the number of combinations that sum up to a certain target. We can fill up this table by iterating over the numbers in `nums` and updating the table accordingly. The final result will be stored in the cell corresponding to the target.

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
        // Create a dp table to store the number of combinations for each target
        vector<int> dp(target + 1, 0);
        
        // Base case: there is one way to sum up to 0 (by not using any numbers)
        dp[0] = 1;
        
        // Fill up the dp table
        for (int i = 1; i <= target; i++) {
            for (int num : nums) {
                if (i - num >= 0) {
                    // If the current number can be used to sum up to the current target,
                    // add the number of combinations that sum up to the remaining target
                    dp[i] += dp[i - num];
                }
            }
        }
        
        // The final result is stored in the cell corresponding to the target
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The dp table should be filled up in a bottom-up manner to avoid using uninitialized values.
- The base case should be handled carefully to ensure the correctness of the solution.