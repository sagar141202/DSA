# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The combination must not be empty, and each number in the combination must be from `nums`. The order of numbers in the combination does matter, and the same number can be used more than once. For example, if `nums = [1, 2, 3]` and `target = 4`, the possible combinations are `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 2, 1]`, `[1, 3]`, `[2, 1, 1]`, `[2, 2]`, `[3, 1]`, so the output is `7`.

## Approach
The problem can be solved using dynamic programming, where we build up a table of combinations that sum up to each number from 1 to the target. We use the previously computed values to compute the number of combinations for the current number. This approach avoids redundant computation and ensures an efficient solution.

## Complexity
- Time: O(target * n), where n is the size of the input array `nums`
- Space: O(target), where target is the target integer

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        // Create a dp array to store the number of combinations for each number from 1 to target
        vector<unsigned int> dp(target + 1, 0);
        
        // Base case: there is one way to make 0, which is to not include any numbers
        dp[0] = 1;
        
        // For each number from 1 to target
        for (int i = 1; i <= target; i++) {
            // For each number in nums
            for (int num : nums) {
                // If the current number is less than or equal to i
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
Input: nums = [1, 2, 3], target = 4
Output: 7
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems and optimal substructure.
- The problem can be broken down into smaller subproblems, and the solutions to these subproblems can be used to compute the solution to the original problem.
- The use of a dp array can help avoid redundant computation and ensure an efficient solution.