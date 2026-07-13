# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. Each element in `nums` can only be used once in a subset. The length of `nums` is between 1 and 200, and the sum of elements in `nums` is between 1 and 10000. For example, given `nums = [1, 5, 11, 5]`, the function should return `true` because the array can be partitioned into `[1, 5, 5]` and `[11]` with equal sum.

## Approach
The problem can be solved using dynamic programming by calculating the possible sum of subsets. We can create a 2D table where each cell represents whether a subset sum is achievable. The algorithm iterates through the array and updates the table accordingly. If the total sum of the array is odd, it is impossible to partition the array into two subsets with equal sum.

## Complexity
- Time: O(n * sum), where n is the number of elements in the array and sum is the total sum of elements in the array.
- Space: O(n * sum), for the 2D table used in dynamic programming.

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
        sum /= 2;
        int n = nums.size();
        vector<vector<bool>> dp(n + 1, vector<bool>(sum + 1, false));
        dp[0][0] = true;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= sum; j++) {
                dp[i][j] = dp[i - 1][j];
                if (j >= nums[i - 1]) {
                    dp[i][j] = dp[i][j] || dp[i - 1][j - nums[i - 1]];
                }
            }
        }
        return dp[n][sum];
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
- The dynamic programming approach is useful for solving problems that have overlapping subproblems.
- The time complexity of the solution depends on the size of the input array and the sum of its elements.
- The problem can be solved using a 2D table to store the achievable subset sums.