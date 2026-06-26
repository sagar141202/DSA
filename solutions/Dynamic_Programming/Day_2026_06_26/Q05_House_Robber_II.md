# House Robber II

## Problem Statement
The problem is a variation of the classic House Robber problem. In this version, the houses are arranged in a circular manner, meaning that the first house is connected to the last house. The goal is to find the maximum amount of money that can be stolen from the houses without stealing from adjacent houses. Each house has a certain amount of money, and the thief can only steal from one house at a time. The constraints are that the input will be a list of integers representing the amount of money in each house, and the output should be the maximum amount of money that can be stolen.

## Approach
The algorithm uses dynamic programming to solve the problem. It breaks down the problem into two sub-problems: one where the first house is robbed and one where the first house is not robbed. The maximum amount of money that can be stolen is then calculated for each sub-problem.

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
        if (nums.size() == 1) return nums[0];
        if (nums.size() == 2) return max(nums[0], nums[1]);

        // Case 1: Rob the first house
        vector<int> dp1(nums.size());
        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
        }

        // Case 2: Do not rob the first house
        vector<int> dp2(nums.size());
        dp2[0] = 0;
        dp2[1] = nums[1];
        for (int i = 2; i < nums.size(); i++) {
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i]);
        }

        return max(dp1[nums.size() - 2], dp2[nums.size() - 1]);
    }
};
```

## Test Cases
```
Input: [2,3,2]
Output: 3
Input: [1,2,3,1]
Output: 4
Input: [0]
Output: 0
```

## Key Takeaways
- The problem can be broken down into two sub-problems: one where the first house is robbed and one where the first house is not robbed.
- Dynamic programming is used to solve each sub-problem.
- The maximum amount of money that can be stolen is calculated for each sub-problem and the maximum of the two is returned.