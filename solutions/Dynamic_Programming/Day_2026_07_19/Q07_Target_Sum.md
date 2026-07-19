# Target Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the number of subsets of the array that sum up to the target. The array can contain both positive and negative integers. The problem can be formalized as follows: find the number of subsets `S` of `nums` such that the sum of the elements in `S` equals `target`. Note that the empty subset is not considered.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array `dp` where `dp[i][j]` represents the number of subsets of the first `i` elements that sum up to `j`. We iterate over the array and for each element, we have two choices: include it in the subset or not. This leads to the recurrence relation `dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]` if `j` is greater than or equal to `nums[i-1]`, and `dp[i][j] = dp[i-1][j]` otherwise.

## Complexity
- Time: O(n*sum), where n is the number of elements in the array and sum is the sum of the absolute values of all elements in the array.
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
        for (int num : nums) {
            sum += abs(num);
        }
        if (abs(target) > sum) return 0;
        
        vector<vector<int>> dp(n + 1, vector<int>(2 * sum + 1, 0));
        dp[0][sum] = 1;
        
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= 2 * sum; j++) {
                if (j - nums[i - 1] >= 0) {
                    dp[i][j] += dp[i - 1][j - nums[i - 1]];
                }
                if (j + nums[i - 1] <= 2 * sum) {
                    dp[i][j] += dp[i - 1][j + nums[i - 1]];
                }
            }
        }
        
        return dp[n][sum + target];
    }
};
```

## Test Cases
```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
```

## Key Takeaways
- The problem requires finding the number of subsets that sum up to a target value, which can be solved using dynamic programming.
- The dynamic programming approach involves maintaining a 2D array to store the number of subsets that sum up to each possible value.
- The time complexity of the solution is O(n*sum), where n is the number of elements and sum is the sum of the absolute values of all elements.