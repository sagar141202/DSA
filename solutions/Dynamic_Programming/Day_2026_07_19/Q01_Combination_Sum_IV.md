# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The problem can be solved using dynamic programming, where we build up a table of combinations for each possible sum from 1 to `target`. For example, if `nums = [1, 2, 3]` and `target = 4`, the combinations are `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 2, 1]`, `[1, 3]`, `[2, 1, 1]`, `[2, 2]`, `[3, 1]`, so the output is `7`.

## Approach
We will use dynamic programming to build up a table of combinations, where `dp[i]` represents the number of combinations that sum up to `i`. We will iterate over each number in `nums` and update `dp[i]` accordingly. The final result will be stored in `dp[target]`.

## Complexity
- Time: O(target * n)
- Space: O(target)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        // Create a dp table to store the number of combinations for each sum
        vector<unsigned int> dp(target + 1, 0);
        dp[0] = 1; // base case: there is one way to sum up to 0 (use no numbers)
        
        // Iterate over each possible sum from 1 to target
        for (int i = 1; i <= target; i++) {
            // Iterate over each number in nums
            for (int num : nums) {
                // If the current number is less than or equal to the current sum
                if (num <= i) {
                    // Update dp[i] by adding the number of combinations that sum up to i - num
                    dp[i] += dp[i - num];
                }
            }
        }
        
        // Return the number of combinations that sum up to target
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
- The `dp` table is used to store the number of combinations for each possible sum.
- The final result is stored in `dp[target]`.