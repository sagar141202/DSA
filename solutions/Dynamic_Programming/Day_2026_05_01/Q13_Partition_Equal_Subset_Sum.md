# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. Each element in the array can only be used once in the partition. The array cannot be modified, and all elements must be used exactly once. The function should return `true` if the array can be partitioned into two subsets with equal sum, otherwise return `false`. The constraint is that 1 <= nums.length <= 200, and 1 <= nums[i] <= 200.

## Approach
The problem can be solved using dynamic programming by calculating the total sum of the array and checking if it's possible to get a subset with a sum equal to half of the total sum. The idea is to build up a table where each cell represents whether a certain sum can be achieved using the first i elements.

## Complexity
- Time: O(n * sum), where n is the number of elements and sum is the total sum of the array
- Space: O(n * sum), for the dynamic programming table

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
        vector<vector<bool>> dp(nums.size() + 1, vector<bool>(target + 1, false));
        dp[0][0] = true;
        for (int i = 1; i <= nums.size(); i++) {
            for (int j = 0; j <= target; j++) {
                dp[i][j] = dp[i - 1][j];
                if (j >= nums[i - 1]) {
                    dp[i][j] = dp[i][j] || dp[i - 1][j - nums[i - 1]];
                }
            }
        }
        return dp[nums.size()][target];
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
- Dynamic programming is used to build up a table of achievable sums.
- The time complexity is proportional to the number of elements and the total sum of the array.