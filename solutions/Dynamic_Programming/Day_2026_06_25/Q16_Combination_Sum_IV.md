# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The problem is a variation of the classic "combination sum" problem, with the added constraint that each number can be used multiple times.

## Approach
The problem can be solved using dynamic programming, where we build up a table of combinations that sum up to each number from 1 to `target`. We iterate over each number in `nums` and update the table accordingly. The final result is stored in the last entry of the table.

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
        // Create a dp table to store the number of combinations that sum up to each number
        vector<int> dp(target + 1, 0);
        
        // Base case: there is one way to sum up to 0 (i.e., not using any numbers)
        dp[0] = 1;
        
        // Iterate over each number from 1 to target
        for (int i = 1; i <= target; i++) {
            // Iterate over each number in nums
            for (int num : nums) {
                // If the current number is less than or equal to i, we can use it in the combination
                if (num <= i) {
                    // Update the dp table accordingly
                    dp[i] += dp[i - num];
                }
            }
        }
        
        // The final result is stored in the last entry of the dp table
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
- The problem can be solved using dynamic programming, where we build up a table of combinations that sum up to each number from 1 to `target`.
- The time complexity is O(n*target), where n is the size of `nums` and `target` is the target sum.
- The space complexity is O(target), where `target` is the target sum.