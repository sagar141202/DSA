# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. Each element in the array can only be used once in the partition. The array has at most 200 elements and the sum of elements is at most 10000. For example, given `nums = [1, 5, 11, 5]`, return `true` because the array can be partitioned as `[1, 5, 5]` and `[11]`, both having a sum of 11.

## Approach
The problem can be solved using dynamic programming by calculating the total sum of the array and checking if it's possible to achieve a sum equal to half of the total sum. We use a DP table to store the achievable sums.

## Complexity
- Time: O(n*sum), where n is the number of elements and sum is the total sum of elements
- Space: O(sum), for the DP table

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
                dp[i] = dp[i] || dp[i - num];
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
Input: nums = [1, 2, 3, 5]
Output: false
```

## Key Takeaways
- The problem requires finding a subset with a sum equal to half of the total sum of the array.
- Dynamic programming is used to store the achievable sums and check if the target sum can be reached.
- The time complexity is O(n*sum), where n is the number of elements and sum is the total sum of elements.