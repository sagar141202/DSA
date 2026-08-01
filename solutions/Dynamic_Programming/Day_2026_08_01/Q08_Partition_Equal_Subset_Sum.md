# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. Each element in the array can only be used once in the partition. The array cannot be modified, and the order of elements does not matter. The function should return `true` if such a partition is possible and `false` otherwise. The constraint is that `1 <= nums.length <= 200` and `1 <= nums[i] <= 100`.

## Approach
The problem can be solved using dynamic programming by calculating the total sum of the array and checking if it's possible to get a subset with a sum equal to half of the total sum. The algorithm iterates over all possible sums from 1 to the target sum and checks if it's possible to achieve each sum using the numbers in the array.

## Complexity
- Time: O(n * sum), where n is the number of elements and sum is the total sum of the array
- Space: O(sum), for the dynamic programming table

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
Input: nums = [1,5,11,5]
Output: true
Input: nums = [1,2,3,5]
Output: false
```

## Key Takeaways
- The problem requires finding a subset with a sum equal to half of the total sum of the array.
- Dynamic programming is used to solve the problem efficiently by avoiding redundant calculations.
- The time complexity depends on the total sum of the array, which can be large if the numbers in the array are large.