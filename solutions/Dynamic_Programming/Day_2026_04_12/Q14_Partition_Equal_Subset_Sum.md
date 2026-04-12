# Partition Equal Subset Sum

## Problem Statement
Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of elements in both subsets is equal, and `false` otherwise. Each element in the array must be used exactly once. The array will only contain non-negative integers, and the sum of all elements in the array will not exceed 2000. For example, given the array `[1, 5, 11, 5]`, the function should return `true` because the array can be partitioned into `[1, 5, 5]` and `[11]`, which have equal sums.

## Approach
We can solve this problem using dynamic programming by calculating the possible sums that can be achieved using the first `i` elements of the array. We will use a boolean array `dp` where `dp[j]` is `true` if the sum `j` can be achieved. The algorithm iterates over the array and updates the `dp` array accordingly.

## Complexity
- Time: O(n * sum), where n is the number of elements in the array and sum is the total sum of the array
- Space: O(sum), where sum is the total sum of the array

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
Input: [1, 5, 11, 5]
Output: true
Input: [1, 2, 3, 5]
Output: false
```

## Key Takeaways
- The problem requires finding a subset of the array that sums up to half of the total sum of the array.
- Dynamic programming is used to efficiently calculate the possible sums that can be achieved using the first `i` elements of the array.
- The time complexity is O(n * sum) and the space complexity is O(sum), where n is the number of elements in the array and sum is the total sum of the array.