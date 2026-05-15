# Target Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the number of subsets of `nums` that sum up to `target`. The array may contain duplicate elements, and each element can only be used once in a subset. For example, given `nums = [1, 1, 1, 1, 1]` and `target = 3`, the subsets that sum up to `target` are `[1, 1, 1]`. The function should return the number of such subsets.

## Approach
The problem can be solved using dynamic programming, where we build a table to store the number of subsets that sum up to each possible total from 0 to `target`. We iterate over the array and update the table accordingly. The final result is stored in the last cell of the table.

## Complexity
- Time: O(n*target)
- Space: O(target)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        
        if (sum < abs(target)) {
            return 0;
        }
        
        int dp[sum * 2 + 1];
        memset(dp, 0, sizeof(dp));
        dp[sum] = 1;
        
        for (int num : nums) {
            int temp[sum * 2 + 1];
            memset(temp, 0, sizeof(temp));
            for (int i = 0; i <= sum * 2; i++) {
                if (dp[i] != 0) {
                    if (i + num <= sum * 2) {
                        temp[i + num] += dp[i];
                    }
                    if (i - num >= 0) {
                        temp[i - num] += dp[i];
                    }
                }
            }
            memcpy(dp, temp, sizeof(dp));
        }
        
        return dp[sum + target];
    }
};
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5
```

## Key Takeaways
- We use a dynamic programming table to store the number of subsets that sum up to each possible total.
- We iterate over the array and update the table accordingly.
- The final result is stored in the last cell of the table, which corresponds to the target sum.