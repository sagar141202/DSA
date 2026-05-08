# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The problem is a variation of the unbounded knapsack problem, where the goal is to find the number of combinations that sum up to a given target.

## Approach
The problem can be solved using dynamic programming, where we build up a table of combinations that sum up to each number from 0 to the target. The algorithm iterates over each number in the array and updates the table accordingly. The final result is stored in the last cell of the table.

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
        // Create a dp array to store the number of combinations that sum up to each number
        vector<int> dp(target + 1, 0);
        
        // Base case: there is one way to sum up to 0 (i.e., not picking any number)
        dp[0] = 1;
        
        // Iterate over each number from 1 to the target
        for (int i = 1; i <= target; i++) {
            // Iterate over each number in the array
            for (int num : nums) {
                // If the current number is less than or equal to the current target
                if (num <= i) {
                    // Update the dp array with the number of combinations that sum up to the current target
                    dp[i] += dp[i - num];
                }
            }
        }
        
        // Return the number of combinations that sum up to the target
        return dp[target];
    }
};
```

## Test Cases
```
Input: nums = [1, 2, 3], target = 4
Output: 7
Explanation: The combinations that sum up to 4 are:
1 + 1 + 1 + 1
1 + 1 + 2
1 + 2 + 1
1 + 3
2 + 1 + 1
2 + 2
3 + 1
```

## Key Takeaways
- The problem can be solved using dynamic programming, where we build up a table of combinations that sum up to each number from 0 to the target.
- The algorithm iterates over each number in the array and updates the table accordingly.
- The final result is stored in the last cell of the table, which represents the number of combinations that sum up to the target.