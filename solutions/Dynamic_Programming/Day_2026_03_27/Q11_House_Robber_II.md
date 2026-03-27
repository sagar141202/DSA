# House Robber II

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob tonight without alerting the police. The street is a circle, meaning the first house is adjacent to the last house.

## Approach
The problem can be solved using dynamic programming by considering two cases: one where the first house is robbed and the last house is not, and another where the first house is not robbed. We will use a bottom-up approach to fill up a DP table.

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

        // Case 1: Rob the first house, don't rob the last house
        vector<int> dp1(n);
        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        for (int i = 2; i < n - 1; i++) {
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
        }

        // Case 2: Don't rob the first house
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
Input: nums = [2,3,2]
Output: 3
Input: nums = [1,2,3,1]
Output: 4
Input: nums = [0]
Output: 0
```

## Key Takeaways
- The problem is a variation of the classic House Robber problem, with the added constraint of the street being a circle.
- We use dynamic programming to solve the problem, considering two cases: one where the first house is robbed and the last house is not, and another where the first house is not robbed.
- The time complexity is O(n) and the space complexity is O(n), where n is the number of houses.