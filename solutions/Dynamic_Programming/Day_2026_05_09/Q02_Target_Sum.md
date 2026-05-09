# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The problem can be formally stated as follows: Given an array `nums` of length `n` and a target sum `target`, return the number of subsets that sum up to `target`. The constraints are: `1 <= n <= 20`, `-10^5 <= nums[i] <= 10^5`, and `-10^6 <= target <= 10^6`. For example, given `nums = [1, 1, 1, 1, 1]` and `target = 3`, the output should be `5` because there are five subsets that sum up to `3`: `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, and `[1, 1, 1]`.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell represents the number of subsets that sum up to a certain value. We can fill this table iteratively by considering each number in the array and updating the table accordingly. The algorithm works by iterating over the array and for each number, it iterates over all possible sums from the target sum down to the current number.

## Complexity
- Time: O(n * target)
- Space: O(n * target)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        int sum = 0;
        for (int num : nums) sum += num;
        
        if (target > sum || target < -sum) return 0;
        
        int offset = sum;
        vector<vector<int>> dp(n, vector<int>(2 * sum + 1, 0));
        
        dp[0][nums[0] + offset] = 1;
        dp[0][-nums[0] + offset] = 1;
        
        for (int i = 1; i < n; i++) {
            for (int j = -sum; j <= sum; j++) {
                if (j - nums[i] >= -sum && j - nums[i] <= sum) {
                    dp[i][j + offset] += dp[i - 1][j - nums[i] + offset];
                }
                if (j + nums[i] >= -sum && j + nums[i] <= sum) {
                    dp[i][j + offset] += dp[i - 1][j + nums[i] + offset];
                }
            }
        }
        
        return dp[n - 1][target + offset];
    }
};
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5
Input: nums = [1], target = 1
Output: 1
```

## Key Takeaways
- The problem can be solved using dynamic programming by building a 2D table.
- The time complexity of the solution is O(n * target) and the space complexity is O(n * target).
- The solution works by iterating over the array and for each number, it iterates over all possible sums from the target sum down to the current number.