# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The combination must not be empty, and the order of the numbers in the combination does not matter. For example, if `nums = [1, 2, 3]` and `target = 4`, the combinations are `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 3]`, and `[2, 2]`, so the output is `4`.

## Approach
We can solve this problem using dynamic programming, where we build up a table of combinations that sum up to each number from 1 to the target. We iterate over each number in the array and update the table accordingly. The final result is stored in the table at the target index.

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
        // Create a dp table to store the number of combinations that sum up to each number
        vector<int> dp(target + 1, 0);
        dp[0] = 1; // There is one way to sum up to 0, which is to not include any number

        // Iterate over each number from 1 to the target
        for (int i = 1; i <= target; i++) {
            // For each number, iterate over each number in the array
            for (int num : nums) {
                // If the current number is less than or equal to the target, update the dp table
                if (i - num >= 0) {
                    dp[i] += dp[i - num];
                }
            }
        }

        // The final result is stored in the dp table at the target index
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
- The order of the numbers in the combination does not matter, so we can use a dynamic programming approach to build up a table of combinations.
- The time complexity is O(n*target) because we iterate over each number in the array and each number from 1 to the target.