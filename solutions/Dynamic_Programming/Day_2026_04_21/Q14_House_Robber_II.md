# House Robber II

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob tonight without alerting the police. The street is a circle, meaning the first house is connected to the last house.

## Approach
The problem can be solved by breaking it down into two sub-problems: one where the first house is robbed and the last house is not, and another where the first house is not robbed. We use dynamic programming to find the maximum amount of money that can be robbed in each case.

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

        // Case 1: Rob the first house, don't rob the last house
        vector<int> dp1(nums.size() - 1);
        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i]);
        }

        // Case 2: Don't rob the first house
        vector<int> dp2(nums.size() - 1);
        dp2[0] = nums[1];
        dp2[1] = max(nums[1], nums[2]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i + 1]);
        }

        return max(dp1[nums.size() - 2], dp2[nums.size() - 2]);
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
- The problem can be broken down into two sub-problems to handle the circular constraint.
- Dynamic programming is used to efficiently solve the sub-problems.
- The maximum amount of money that can be robbed is the maximum of the two sub-problems.