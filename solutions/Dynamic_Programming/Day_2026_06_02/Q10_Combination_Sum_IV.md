# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The problem can be solved using dynamic programming, where we build up a table of combinations for each number up to the target. For example, if `nums = [1, 2, 3]` and `target = 4`, the output should be `7` because there are 7 combinations that sum up to 4: `[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]`.

## Approach
We will use a dynamic programming approach to solve this problem, where we build up a table of combinations for each number up to the target. The idea is to calculate the number of combinations for each number `i` by considering all numbers in `nums` that are less than or equal to `i`. We will use a bottom-up approach to fill up the table.

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
        // Create a dp table to store the number of combinations for each number up to the target
        vector<int> dp(target + 1, 0);
        
        // Base case: there is one way to make 0, which is to not include any numbers
        dp[0] = 1;
        
        // Fill up the dp table
        for (int i = 1; i <= target; i++) {
            // For each number up to the target, consider all numbers in nums that are less than or equal to i
            for (int num : nums) {
                if (i >= num) {
                    // The number of combinations for i is the sum of the number of combinations for i - num and the number of combinations for i without using num
                    dp[i] += dp[i - num];
                }
            }
        }
        
        // The answer is the number of combinations for the target
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
- The problem can be solved using a dynamic programming approach with a time complexity of O(target * n) and a space complexity of O(target).
- The idea is to calculate the number of combinations for each number up to the target by considering all numbers in `nums` that are less than or equal to the current number.
- The base case is that there is one way to make 0, which is to not include any numbers.