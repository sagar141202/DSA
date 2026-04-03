# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the array will not exceed 200. Each element in the array will be in the range [1, 100]. The sum of all elements in the array will not exceed 1000. For example, given `nums = [1, 5, 11, 5]`, the output should be `true` because the array can be partitioned into `[1, 5, 5]` and `[11]` with equal sum. Given `nums = [1, 2, 3, 9]`, the output should be `false` because the array cannot be partitioned into two subsets with equal sum.

## Approach
The problem can be solved using dynamic programming by calculating the total sum of the array and checking if it's possible to get a subset with sum equal to half of the total sum. We use a boolean array `dp` where `dp[i]` is `true` if it's possible to get a sum `i`. The algorithm iterates over the array and updates the `dp` array accordingly.

## Complexity
- Time: O(n * sum)
- Space: O(sum)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (sum % 2 != 0) {
            return false;
        }
        int target = sum / 2;
        vector<bool> dp(target + 1, false);
        dp[0] = true;
        for (int num : nums) {
            for (int i = target; i >= num; i--) {
                if (dp[i - num]) {
                    dp[i] = true;
                }
            }
        }
        return dp[target];
    }
};
```

## Test Cases
```
Input: nums = [1, 5, 11, 5]
Output: true
Input: nums = [1, 2, 3, 9]
Output: false
```

## Key Takeaways
- The problem requires finding a subset with sum equal to half of the total sum of the array.
- Dynamic programming is used to solve the problem efficiently by avoiding redundant calculations.
- The time complexity is O(n * sum) where n is the length of the array and sum is the total sum of the array.