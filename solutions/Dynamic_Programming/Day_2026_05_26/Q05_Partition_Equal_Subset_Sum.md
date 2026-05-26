# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the array will not exceed 200. Each element in the array will be in the range [1, 100]. The array may contain duplicate elements. For example, given `nums = [1, 5, 11, 5]`, the function should return `true` because the array can be partitioned into `[1, 5, 5]` and `[11]`.

## Approach
The problem can be solved using dynamic programming by calculating the total sum of the array and checking if it's possible to get a subset with a sum equal to half of the total sum. The algorithm iterates over all possible subset sums and checks if the current number can be included in the subset.

## Complexity
- Time: O(n * sum), where n is the number of elements in the array and sum is the total sum of the array elements.
- Space: O(sum), for storing the dynamic programming table.

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
Input: nums = [1, 2, 3, 5]
Output: false
```

## Key Takeaways
- The problem can be solved using dynamic programming by calculating the total sum of the array and checking if it's possible to get a subset with a sum equal to half of the total sum.
- The algorithm iterates over all possible subset sums and checks if the current number can be included in the subset.
- The time complexity is O(n * sum), where n is the number of elements in the array and sum is the total sum of the array elements.