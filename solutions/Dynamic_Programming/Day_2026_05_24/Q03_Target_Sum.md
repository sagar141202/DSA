# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets of the array that sum up to the target. The array can contain both positive and negative integers. The problem can be formally stated as: given an array `nums` and an integer `target`, return the number of subsets of `nums` that sum up to `target`. For example, if `nums = [1, 1, 1, 1, 1]` and `target = 3`, the output should be `5`, because there are `5` subsets that sum up to `3`: `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, and `[1, 1, 1]`. The constraints are: `1 <= nums.size() <= 20` and `0 <= nums[i] <= 50`.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the number of subsets that sum up to each possible target value. We iterate over the array and update the table accordingly. The algorithm uses a bottom-up approach to fill the table.

## Complexity
- Time: O(n * sum), where n is the size of the array and sum is the sum of all elements in the array
- Space: O(n * sum)

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
        
        // if the target is greater than the sum of all elements, return 0
        if (abs(target) > sum) return 0;
        
        // create a 2D table to store the number of subsets that sum up to each target value
        int dp[n + 1][2 * sum + 1] = {};
        
        // base case: there is one way to get a sum of 0 with an empty subset
        dp[0][sum] = 1;
        
        // fill the table
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < 2 * sum + 1; j++) {
                // if the current element is less than or equal to the current target value
                if (j - nums[i - 1] >= 0) {
                    dp[i][j] += dp[i - 1][j - nums[i - 1]];
                }
                // if the current element is greater than or equal to the current target value
                if (j + nums[i - 1] < 2 * sum + 1) {
                    dp[i][j] += dp[i - 1][j + nums[i - 1]];
                }
            }
        }
        
        // return the number of subsets that sum up to the target
        return dp[n][sum + target];
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
- The problem can be solved using dynamic programming with a 2D table to store the number of subsets that sum up to each target value.
- The time complexity is O(n * sum), where n is the size of the array and sum is the sum of all elements in the array.
- The space complexity is O(n * sum), which is used to store the 2D table.