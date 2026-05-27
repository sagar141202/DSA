# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The combination must not be empty, and the order of the numbers in the combination does not matter. For example, if `nums = [1, 2, 3]` and `target = 4`, the possible combinations are `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 3]`, and `[2, 2]`, so the output should be `4`.

## Approach
The problem can be solved using dynamic programming, where we build up a table of combinations that sum up to each number from 1 to the target. We iterate over each number in the table and update the combinations that sum up to the current number by adding the combinations that sum up to the current number minus each number in the input array.

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
        // Create a dynamic programming table to store the number of combinations that sum up to each number
        vector<int> dp(target + 1, 0);
        dp[0] = 1;  // Base case: there is one way to sum up to 0 (i.e., not using any numbers)

        // Iterate over each number in the table
        for (int i = 1; i <= target; i++) {
            // Iterate over each number in the input array
            for (int num : nums) {
                // If the current number is greater than or equal to the number in the input array
                if (i >= num) {
                    // Update the combinations that sum up to the current number
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
Input: nums = [9], target = 3
Output: 0
```

## Key Takeaways
- The problem can be solved using dynamic programming with a time complexity of O(target * n) and a space complexity of O(target).
- The dynamic programming table is used to store the number of combinations that sum up to each number from 1 to the target.
- The table is updated by iterating over each number in the table and adding the combinations that sum up to the current number minus each number in the input array.