# House Robber II

## Problem Statement
The problem is a variation of the classic House Robber problem, where we have a circular array of houses, and we want to find the maximum amount of money we can rob without robbing two adjacent houses. The constraint is that we cannot rob the first and last house at the same time, since they are considered adjacent in the circular array. We are given an array of integers representing the amount of money in each house, and we need to find the maximum amount of money we can rob.

## Approach
We will use dynamic programming to solve this problem, breaking it down into two cases: one where we rob the first house and one where we don't. We will then find the maximum amount of money we can rob in each case.

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
        if (n == 1) return nums[0];
        if (n == 2) return max(nums[0], nums[1]);

        // Case 1: Rob the first house
        vector<int> dp1(n);
        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        for (int i = 2; i < n - 1; i++) {
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i]);
        }

        // Case 2: Don't rob the first house
        vector<int> dp2(n);
        dp2[0] = 0;
        dp2[1] = nums[1];
        for (int i = 2; i < n; i++) {
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i]);
        }

        return max(dp1[n - 2], dp2[n - 1]);
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
- The problem can be broken down into two cases: one where we rob the first house and one where we don't.
- We use dynamic programming to solve each case, finding the maximum amount of money we can rob in each case.
- The final answer is the maximum of the two cases.