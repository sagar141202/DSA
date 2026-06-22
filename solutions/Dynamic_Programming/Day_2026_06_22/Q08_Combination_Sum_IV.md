# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The order of the numbers in the combination does not matter. For example, given `nums = [1, 2, 3]` and `target = 4`, the combinations are `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 3]`, and `[2, 2]`, so the output is `4`.

## Approach
The problem can be solved using dynamic programming by building up a table of combinations for each sum from 1 to the target. The number of combinations for each sum is the sum of the number of combinations for the sums that are less than the current sum by each number in the array.

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
        // Create a dp array to store the number of combinations for each sum
        vector<int> dp(target + 1, 0);
        
        // Base case: there is one way to get a sum of 0 (by not using any numbers)
        dp[0] = 1;
        
        // For each sum from 1 to the target
        for (int i = 1; i <= target; i++) {
            // For each number in the array
            for (int num : nums) {
                // If the current number is less than or equal to the current sum
                if (num <= i) {
                    // Add the number of combinations for the sum minus the current number
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
Input: nums = [9], target = 3
Output: 0
```

## Key Takeaways
- Use dynamic programming to build up a table of combinations for each sum.
- The number of combinations for each sum is the sum of the number of combinations for the sums that are less than the current sum by each number in the array.
- The time complexity is O(n*target) and the space complexity is O(target), where n is the number of distinct integers in the array.