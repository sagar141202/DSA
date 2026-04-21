# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of ways to assign + or - sign to each integer in the array such that the sum of the resulting array equals the target sum. The array contains only non-negative integers, and the target sum can be any integer. The length of the array is at most 20, and each integer in the array is at most 1000. For example, given the array [1, 1, 1, 1, 1] and the target sum 3, there are 5 ways to achieve the target sum: [1, 1, 1, -1, -1], [1, 1, -1, 1, -1], [1, 1, -1, -1, 1], [1, -1, 1, 1, -1], and [1, -1, 1, -1, 1].

## Approach
The problem can be solved using dynamic programming. We can calculate the number of ways to reach each possible sum from -total_sum to total_sum, where total_sum is the sum of all integers in the array. We initialize a dp array with size 2 * total_sum + 1, and then iterate over the array and update the dp array accordingly.

## Complexity
- Time: O(n * total_sum)
- Space: O(total_sum)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findTargetSumWays(vector<int>& nums, int target) {
    int total_sum = 0;
    for (int num : nums) {
        total_sum += num;
    }
    if (target > total_sum || target < -total_sum) {
        return 0;
    }
    int offset = total_sum;
    vector<int> dp(2 * total_sum + 1, 0);
    dp[offset] = 1;
    for (int num : nums) {
        vector<int> next_dp(2 * total_sum + 1, 0);
        for (int i = 0; i < 2 * total_sum + 1; i++) {
            if (dp[i] != 0) {
                next_dp[i + num] += dp[i];
                next_dp[i - num] += dp[i];
            }
        }
        dp = next_dp;
    }
    return dp[offset + target];
}
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5
Input: nums = [1], target = 1
Output: 1
```

## Key Takeaways
- The problem can be solved using dynamic programming with a time complexity of O(n * total_sum) and a space complexity of O(total_sum).
- We need to initialize the dp array with size 2 * total_sum + 1 to account for all possible sums from -total_sum to total_sum.
- We can use a offset to simplify the calculation and avoid dealing with negative indices.