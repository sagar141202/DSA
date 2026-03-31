# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The answer is guaranteed to fit within a 32-bit integer.

## Approach
The problem can be solved using dynamic programming, where we build up a table of combinations that sum up to each number from 1 to the target. We use the previously computed values to calculate the number of combinations for the current number. This approach ensures that we avoid redundant calculations and optimize the solution.

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
        // Create a dp table to store the number of combinations for each number
        vector<int> dp(target + 1, 0);
        dp[0] = 1; // base case: one way to sum up to 0 (use no numbers)

        // Fill up the dp table
        for (int i = 1; i <= target; i++) {
            for (int num : nums) {
                if (i - num >= 0) {
                    dp[i] += dp[i - num];
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
Explanation: The possible combination ways are:
- 1 + 1 + 1 + 1
- 1 + 1 + 2
- 1 + 2 + 1
- 1 + 3
- 2 + 1 + 1
- 2 + 2
- 3 + 1
```

## Key Takeaways
- Dynamic programming is a powerful technique for solving problems that have overlapping subproblems.
- The key to solving this problem is to recognize that the number of combinations that sum up to a given number can be calculated using the previously computed values.
- The time complexity of the solution is O(target * n), where n is the number of distinct integers in the input array.