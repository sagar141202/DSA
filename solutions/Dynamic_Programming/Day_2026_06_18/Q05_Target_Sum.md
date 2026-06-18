# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The problem can be formalized as follows: Given an array `arr` of size `n` and a target sum `target`, find the number of subsets of `arr` that sum up to `target`. The array `arr` can contain duplicate elements.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell `[i][j]` represents the number of subsets of the array from index `0` to `i` that sum up to `j`. The final result will be stored in the cell `[n][target]`.

## Complexity
- Time: O(n*sum)
- Space: O(n*sum)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findTargetSumWays(vector<int>& nums, int target) {
    int n = nums.size();
    int sum = 0;
    for (int num : nums) sum += num;
    
    if (target > sum || target < -sum) return 0;
    
    int dp[n][2*sum + 1];
    memset(dp, 0, sizeof(dp));
    
    dp[0][nums[0] + sum] = 1;
    dp[0][-nums[0] + sum] = 1;
    
    for (int i = 1; i < n; i++) {
        for (int j = -sum; j <= sum; j++) {
            if (dp[i-1][j + sum] > 0) {
                dp[i][j + nums[i] + sum] += dp[i-1][j + sum];
                dp[i][j - nums[i] + sum] += dp[i-1][j + sum];
            }
        }
    }
    
    return dp[n-1][target + sum];
}
```

## Test Cases
```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
```

## Key Takeaways
- The dynamic programming approach is useful for solving problems that have overlapping subproblems.
- The time complexity of the solution is O(n*sum) where n is the size of the array and sum is the sum of all elements in the array.
- The space complexity of the solution is O(n*sum) for storing the dynamic programming table.