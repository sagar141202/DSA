# House Robber II

## Problem Statement
The problem is a variation of the classic House Robber problem. You are a thief who wants to rob houses in a circular neighborhood, where each house has a certain amount of money. The constraint is that you cannot rob two adjacent houses. The goal is to find the maximum amount of money you can rob. The input is an array of integers representing the amount of money in each house, and the output is the maximum amount of money that can be robbed.

## Approach
The algorithm uses dynamic programming to solve the problem. It calculates the maximum amount of money that can be robbed up to each house, considering two cases: robbing the current house and not robbing the current house. The maximum amount of money that can be robbed is the maximum of these two cases.

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
        
        // Case 1: Rob the first house, cannot rob the last house
        vector<int> dp1(nums.size());
        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
        }
        
        // Case 2: Do not rob the first house, can rob the last house
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
Input: nums = [2,3,2]
Output: 3
Input: nums = [1,2,3,1]
Output: 4
Input: nums = [0]
Output: 0
```

## Key Takeaways
- The problem can be solved using dynamic programming by considering two cases: robbing the first house and not robbing the first house.
- The maximum amount of money that can be robbed is the maximum of these two cases.
- The time complexity is O(n) and the space complexity is O(n), where n is the number of houses.