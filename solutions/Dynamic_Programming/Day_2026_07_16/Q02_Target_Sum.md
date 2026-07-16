# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The problem can be formally defined as: given an array `nums` of size `n` and an integer `target`, return the number of subsets that sum up to `target`. The constraints are: `1 <= n <= 20`, `-10^6 <= nums[i] <= 10^6`, and `-10^6 <= target <= 10^6`. For example, if `nums = [1, 1, 1, 1, 1]` and `target = 3`, the output should be `5`.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the number of subsets that sum up to each possible sum. The table is filled in a bottom-up manner, and the final result is stored in the last cell of the table. We consider two cases for each number: include it in the subset or exclude it.

## Complexity
- Time: O(n * sum), where n is the size of the array and sum is the sum of all numbers in the array
- Space: O(n * sum), where n is the size of the array and sum is the sum of all numbers in the array

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        
        // If the target is greater than the sum of all numbers or less than the negative sum of all numbers, return 0
        if (target > sum || target < -sum) {
            return 0;
        }
        
        int dp[n][2 * sum + 1];
        dp[0][sum + nums[0]] = 1;
        dp[0][sum - nums[0]] = 1;
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= 2 * sum; j++) {
                if (j - nums[i] >= 0) {
                    dp[i][j] += dp[i - 1][j - nums[i]];
                }
                if (j + nums[i] <= 2 * sum) {
                    dp[i][j] += dp[i - 1][j + nums[i]];
                }
            }
        }
        
        return dp[n - 1][sum + target];
    }
};
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5

Input: nums = [1], target = 1
Output: 1

Input: nums = [1, 0], target = 1
Output: 2
```

## Key Takeaways
- The problem can be solved using dynamic programming by building a 2D table to store the number of subsets that sum up to each possible sum.
- The time complexity is O(n * sum), where n is the size of the array and sum is the sum of all numbers in the array.
- The space complexity is O(n * sum), where n is the size of the array and sum is the sum of all numbers in the array.