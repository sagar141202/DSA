# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The solution should be able to handle large inputs and should have an optimal time and space complexity. For example, if `nums = [1, 2, 3]` and `target = 4`, the output should be `7` because there are `7` combinations that sum up to `4`: `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 2, 1]`, `[1, 3]`, `[2, 1, 1]`, `[2, 2]`, `[3, 1]`.

## Approach
The problem can be solved using dynamic programming. We can create a DP array where each index represents a sum from 0 to the target, and the value at each index represents the number of combinations that sum up to that index. We can then fill up the DP array by iterating over the numbers in `nums` and updating the values in the DP array accordingly.

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
        // Create a DP array to store the number of combinations for each sum
        vector<unsigned int> dp(target + 1, 0);
        
        // Base case: there is one way to get a sum of 0 (by not choosing any numbers)
        dp[0] = 1;
        
        // Fill up the DP array
        for (int i = 1; i <= target; i++) {
            // For each number in nums, update the value in the DP array
            for (int num : nums) {
                if (i - num >= 0) {
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
- The problem can be solved using dynamic programming with a time complexity of O(n*target) and a space complexity of O(target).
- The DP array should be initialized with a size of `target + 1` to accommodate the base case where the sum is 0.
- The base case should be handled by setting the value at index 0 of the DP array to 1, representing the fact that there is one way to get a sum of 0 (by not choosing any numbers).