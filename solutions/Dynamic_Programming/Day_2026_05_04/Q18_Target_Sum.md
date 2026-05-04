# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The problem can be formalized as follows: Given an array `arr` of size `n` and a target sum `target`, find the number of subsets of `arr` that sum up to `target`. The constraints are: `1 <= n <= 100`, `-10^5 <= arr[i] <= 10^5`, and `0 <= target <= 10^5`.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the number of subsets that sum up to each possible sum from 0 to the target sum. The algorithm iterates over the array and updates the table accordingly. The final answer is stored in the cell corresponding to the target sum.

## Complexity
- Time: O(n * target)
- Space: O(n * target)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        int sum = 0;
        for (int num : nums) sum += num;
        
        // If the target sum is greater than the total sum or less than the negative total sum, return 0
        if (target > sum || target < -sum) return 0;
        
        // Initialize a 2D table to store the number of subsets that sum up to each possible sum
        int dp[n + 1][2 * sum + 1] = {0};
        
        // Base case: there is one subset that sums up to 0 (the empty subset)
        dp[0][sum] = 1;
        
        // Iterate over the array and update the table
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= 2 * sum; j++) {
                if (j - nums[i - 1] >= 0) dp[i][j] += dp[i - 1][j - nums[i - 1]];
                if (j + nums[i - 1] <= 2 * sum) dp[i][j] += dp[i - 1][j + nums[i - 1]];
            }
        }
        
        // The final answer is stored in the cell corresponding to the target sum
        return dp[n][sum + target];
    }
};
```

## Test Cases
```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Input: nums = [1], target = 1
Output: 1
```

## Key Takeaways
- The problem can be solved using dynamic programming by building a 2D table to store the number of subsets that sum up to each possible sum.
- The time complexity is O(n * target) and the space complexity is O(n * target), where n is the size of the array and target is the target sum.
- The solution can be optimized by using a 1D table instead of a 2D table, but this would require more complex logic to update the table.