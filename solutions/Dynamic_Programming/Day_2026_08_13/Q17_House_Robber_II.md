# House Robber II

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police. The street is a circle, meaning the first house is adjacent to the last house.

## Approach
The problem can be broken down into two sub-problems: rob the first house or not. We use dynamic programming to find the maximum amount of money that can be robbed in each case.

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
        
        // rob the first house
        vector<int> dp1(nums.size(), 0);
        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
        }
        
        // not rob the first house
        vector<int> dp2(nums.size(), 0);
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
- The problem is a variation of the classic House Robber problem with a circular constraint.
- We can break down the problem into two sub-problems: rob the first house or not.
- Dynamic programming is used to find the maximum amount of money that can be robbed in each case.