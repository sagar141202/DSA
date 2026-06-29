# House Robber II

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed. All houses in this place are arranged in a circle, meaning the first house is connected to the last one. You cannot rob adjacent houses. Given a list of non-negative integers representing the amount of money in each house, determine the maximum amount of money you can rob without robbing adjacent houses. The list of houses is in a circular arrangement, so the first and last houses are considered adjacent.

## Approach
This problem can be solved using dynamic programming, where we break down the problem into two sub-problems: one where we rob the first house and one where we do not rob the first house. We then find the maximum amount of money we can rob in each case.

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
        
        // case 1: rob the first house
        vector<int> dp1(nums.size());
        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
        }
        
        // case 2: do not rob the first house
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
- To solve this problem, we need to consider two separate cases: one where we rob the first house and one where we do not rob the first house.
- We use dynamic programming to find the maximum amount of money we can rob in each case.
- The time complexity is O(n) because we make two passes through the list of houses. The space complexity is also O(n) because we need to store the maximum amount of money we can rob at each house.