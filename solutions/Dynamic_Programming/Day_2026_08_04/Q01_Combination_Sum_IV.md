# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The answer is guaranteed to fit within a 32-bit integer.

## Approach
We will use dynamic programming to solve this problem, where we build up a table of solutions to subproblems. The idea is to calculate the number of combinations that sum up to each number from 1 to `target`. We will use the previously computed values to compute the current value.

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
        vector<int> dp(target + 1, 0);
        dp[0] = 1;  // Base case: there is one way to sum up to 0 (use no numbers)

        // For each possible sum from 1 to target
        for (int i = 1; i <= target; i++) {
            // For each number in nums
            for (int num : nums) {
                // If the current number is less than or equal to the current sum
                if (num <= i) {
                    // Add the number of combinations that sum up to i - num to dp[i]
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
Input: nums = [1,2,3], target = 4
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
- Use dynamic programming to solve problems that have overlapping subproblems.
- The order of the numbers in the combination does not matter.
- We can use the previously computed values to compute the current value, which reduces the time complexity of the solution.