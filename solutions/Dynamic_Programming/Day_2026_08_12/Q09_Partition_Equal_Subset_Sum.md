# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the array will not exceed 200. Each element in the array will be between 1 and 100, and the total sum of elements will not exceed 1000. For example, given `nums = [1, 5, 11, 5]`, the output should be `true` because the array can be partitioned into `[1, 5, 5]` and `[11]`, which have equal sums.

## Approach
This problem can be solved using dynamic programming by calculating the total sum of the array and checking if it's possible to reach half of the sum using the elements of the array. The algorithm iterates over each element in the array and updates a dynamic programming table to track the reachable sums.

## Complexity
- Time: O(n * sum), where n is the number of elements and sum is the total sum of the array
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
- The problem can be solved using dynamic programming to track the reachable sums.
- The time complexity is O(n * sum), where n is the number of elements and sum is the total sum of the array.
- The space complexity is O(sum), where sum is the total sum of the array.