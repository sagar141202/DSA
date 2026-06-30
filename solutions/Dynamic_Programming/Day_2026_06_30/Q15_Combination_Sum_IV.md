# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The problem is a classic example of unbounded knapsack problem. For example, if `nums = [1, 2, 3]` and `target = 4`, the combinations are `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 3]`, and `[2, 2]`, so the output is `4`.

## Approach
We can solve this problem using dynamic programming, where we build up a table of combinations for each sum from 1 to the target. The algorithm uses the concept of unbounded knapsack, where each number can be used any number of times. We iterate over each number in `nums` and update the combinations for each sum.

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
        // Create a dp array to store the combinations for each sum
        vector<int> dp(target + 1, 0);
        
        // Base case: there is one way to sum up to 0 (i.e., not using any numbers)
        dp[0] = 1;
        
        // Iterate over each sum from 1 to the target
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
- Dynamic programming is a powerful technique for solving problems with overlapping subproblems.
- The unbounded knapsack problem is a classic example of dynamic programming, where each item can be used any number of times.
- The time complexity of the solution is O(n*target), where n is the number of distinct integers in `nums`.