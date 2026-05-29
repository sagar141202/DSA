# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The problem statement is similar to the unbounded knapsack problem. For example, if `nums = [1, 2, 3]` and `target = 4`, the possible combinations are `1+1+1+1`, `1+1+2`, `1+3`, `2+2`, so the output is `4`.

## Approach
The problem can be solved using dynamic programming, where we build up a table of combinations for each possible sum from 1 to the target. We iterate over each number in `nums` and update the combinations for each sum. The key idea is to use the previously computed combinations to compute the combinations for the current sum.

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
        // Create a dp table to store the combinations for each sum
        vector<int> dp(target + 1, 0);
        
        // Base case: there is one way to get a sum of 0 (by not using any numbers)
        dp[0] = 1;
        
        // Iterate over each possible sum from 1 to the target
        for (int i = 1; i <= target; i++) {
            // Iterate over each number in nums
            for (int num : nums) {
                // If the current number is less than or equal to the current sum
                if (num <= i) {
                    // Update the combinations for the current sum
                    dp[i] += dp[i - num];
                }
            }
        }
        
        // Return the combinations for the target sum
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
- The problem can be solved using dynamic programming with a time complexity of O(n*target) and a space complexity of O(target).
- The key idea is to use the previously computed combinations to compute the combinations for the current sum.
- The problem statement is similar to the unbounded knapsack problem, but with a different objective function.