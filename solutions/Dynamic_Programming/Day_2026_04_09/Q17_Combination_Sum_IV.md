# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The order of the numbers in the combination does not matter. For example, if `nums = [1, 2, 3]` and `target = 4`, the possible combinations are `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 3]`, and `[2, 2]`, so the output is `4`.

## Approach
The problem can be solved using dynamic programming, where we build up a table of combinations for each number up to the target. We initialize the table with a base case where there is one way to reach a sum of 0 (by not choosing any numbers). Then, for each number up to the target, we calculate the number of combinations by considering all possible ways to reach the current sum using the numbers in `nums`.

## Complexity
- Time: O(target * n), where n is the size of `nums`
- Space: O(target)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        // Create a table to store the number of combinations for each sum
        vector<int> dp(target + 1, 0);
        
        // Base case: there is one way to reach a sum of 0
        dp[0] = 1;
        
        // For each number up to the target
        for (int i = 1; i <= target; i++) {
            // For each number in nums
            for (int num : nums) {
                // If the current number is less than or equal to the current sum
                if (num <= i) {
                    // Add the number of combinations for the remaining sum to the current sum
                    dp[i] += dp[i - num];
                }
            }
        }
        
        // Return the number of combinations for the target sum
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
- The problem can be solved using dynamic programming with a time complexity of O(target * n) and a space complexity of O(target).
- The order of the numbers in the combination does not matter, so we only need to consider the sum of the numbers.
- The base case is that there is one way to reach a sum of 0 (by not choosing any numbers).