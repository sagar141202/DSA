# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used an unlimited number of times in the combination. The answer is guaranteed to fit within a 32-bit integer.

## Approach
The problem can be solved using dynamic programming, where we build up a table of combinations for each number up to the target. We initialize a table `dp` of size `target + 1` with `dp[0] = 1`, since there is one way to sum up to 0 (by not using any numbers). Then, for each number `i` from 1 to `target`, we update `dp[i]` by adding the number of combinations that sum up to `i - num` for each `num` in `nums`.

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
        // Create a table to store the number of combinations for each number up to target
        vector<int> dp(target + 1, 0);
        // Initialize dp[0] to 1, since there is one way to sum up to 0
        dp[0] = 1;
        
        // For each number i from 1 to target
        for (int i = 1; i <= target; i++) {
            // For each number num in nums
            for (int num : nums) {
                // If i is greater than or equal to num
                if (i >= num) {
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
- The problem can be solved using dynamic programming, where we build up a table of combinations for each number up to the target.
- The time complexity is O(target * n), where n is the number of distinct integers in the input array.
- The space complexity is O(target), since we need to store the number of combinations for each number up to the target.