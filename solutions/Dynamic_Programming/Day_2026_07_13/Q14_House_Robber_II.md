# House Robber II

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed. All houses are arranged in a circle, meaning the first house is connected to the last house. You cannot rob adjacent houses. Given a list of non-negative integers representing the amount of money in each house, determine the maximum amount of money you can rob.

## Approach
The problem can be solved using dynamic programming by breaking it down into two cases: one where the first house is robbed and another where the first house is not robbed. We will calculate the maximum amount that can be robbed in both cases and return the maximum of the two.

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
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];

        // Case 1: First house is robbed
        vector<int> dp1(n);
        dp1[0] = nums[0];
        dp1[1] = nums[0];
        for (int i = 2; i < n; i++) {
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
        }

        // Case 2: First house is not robbed
        vector<int> dp2(n);
        dp2[0] = 0;
        dp2[1] = nums[1];
        for (int i = 2; i < n; i++) {
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i]);
        }

        return max(dp1[n-2], dp2[n-1]);
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
- The problem is a variation of the classic House Robber problem, with the added constraint of the houses being arranged in a circle.
- Dynamic programming is used to solve the problem by breaking it down into two cases and calculating the maximum amount that can be robbed in each case.
- The time complexity is O(n) and the space complexity is O(n), where n is the number of houses.