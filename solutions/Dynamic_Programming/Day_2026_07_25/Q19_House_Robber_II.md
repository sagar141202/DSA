# House Robber II

## Problem Statement
The problem is a variation of the classic House Robber problem. In this version, the houses are arranged in a circle, meaning that the first and last houses are adjacent to each other. The goal is to find the maximum amount of money that can be stolen from the houses without stealing from two adjacent houses. Each house has a certain amount of money, and the amount of money in each house is given in an array. The constraints are that we cannot steal from the first and last house at the same time, and we cannot steal from two adjacent houses.

## Approach
The approach is to use dynamic programming to solve the problem. We will consider two cases: one where we steal from the first house, and one where we do not steal from the first house. In each case, we will use a dynamic programming array to keep track of the maximum amount of money that can be stolen up to each house.

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
        
        // case 1: steal from the first house
        vector<int> dp1(n);
        dp1[0] = nums[0];
        dp1[1] = nums[0];
        for (int i = 2; i < n - 1; i++) {
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i]);
        }
        
        // case 2: do not steal from the first house
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
- The dynamic programming approach is useful for solving problems that have overlapping subproblems.
- The problem can be broken down into two cases: one where we steal from the first house, and one where we do not steal from the first house.
- The time complexity is O(n) because we are iterating over the array twice, once for each case.