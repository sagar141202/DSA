# House Robber II

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police. The twist in this problem is that the first and the last house are also considered adjacent.

## Approach
The problem can be solved using dynamic programming. We will consider two cases: one where we rob the first house and one where we don't. For each case, we will calculate the maximum amount of money that can be robbed.

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
        vector<int> dp1(nums.size() - 1);
        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
        }

        // Case 2: Don't rob the first house
        vector<int> dp2(nums.size() - 1);
        dp2[0] = nums[1];
        dp2[1] = max(nums[1], nums[2]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i+1]);
        }

        return max(dp1.back(), dp2.back());
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
- The problem can be broken down into two sub-problems: one where we rob the first house and one where we don't.
- Dynamic programming can be used to solve each sub-problem efficiently.
- The maximum amount of money that can be robbed is the maximum of the two sub-problems.