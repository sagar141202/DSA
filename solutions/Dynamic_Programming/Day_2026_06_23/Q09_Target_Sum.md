# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The target sum can also be positive or negative. The problem can be formalized as follows: Given an array `nums` of size `n` and an integer `target`, return the number of subsets that sum up to `target`. For example, if `nums = [1, 1, 1, 1, 1]` and `target = 3`, the output should be `5` because there are `5` subsets that sum up to `3`: `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, and `[1, 1, 1]`.

## Approach
This problem can be solved using dynamic programming, where we build a 2D table to store the number of subsets that sum up to each possible sum. We iterate over the array and for each element, we update the table with the number of subsets that sum up to the current sum minus the current element. The final answer will be stored in the table at the index corresponding to the target sum.

## Complexity
- Time: O(n*sum)
- Space: O(n*sum)

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
        
        // If the target is greater than the sum of all elements or less than the negative sum of all elements, return 0
        if (target > sum || target < -sum) return 0;
        
        // Create a 2D table to store the number of subsets that sum up to each possible sum
        vector<vector<int>> dp(n, vector<int>(2*sum+1, 0));
        
        // Initialize the table with the base case
        dp[0][sum+nums[0]] = 1;
        dp[0][sum-nums[0]] = 1;
        
        // Fill the table in a bottom-up manner
        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= 2*sum; j++) {
                if (j-nums[i] >= 0) dp[i][j] += dp[i-1][j-nums[i]];
                if (j+nums[i] <= 2*sum) dp[i][j] += dp[i-1][j+nums[i]];
            }
        }
        
        // The final answer is stored in the table at the index corresponding to the target sum
        return dp[n-1][sum+target];
    }
};
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5
Input: nums = [1], target = 1
Output: 1
```

## Key Takeaways
- The problem can be solved using dynamic programming by building a 2D table to store the number of subsets that sum up to each possible sum.
- The time complexity is O(n*sum) and the space complexity is O(n*sum), where n is the size of the input array and sum is the sum of all elements in the array.
- The problem requires careful handling of edge cases, such as when the target sum is greater than the sum of all elements or less than the negative sum of all elements.