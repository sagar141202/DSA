# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob tonight without alerting the police. The first and last houses are also considered adjacent.

## Approach
The problem can be solved using dynamic programming by maintaining two variables to track the maximum amount of money that can be robbed up to the current house. The algorithm iterates through the houses, updating these variables based on whether the current house is robbed or not.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return nums[0];

        vector<int> dp(nums.size());
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);

        for (int i = 2; i < nums.size(); i++) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }

        return dp[nums.size()-1];
    }
};
```

## Test Cases
```
Input: [1,2,3,1]
Output: 4
Input: [2,7,9,3,1]
Output: 12
```

## Key Takeaways
- The dynamic programming approach helps to avoid redundant calculations by storing the results of subproblems in the `dp` array.
- The base cases are handled before the main loop to ensure the algorithm works correctly for arrays of size 0 and 1.
- The time complexity is linear, making the solution efficient for large inputs.