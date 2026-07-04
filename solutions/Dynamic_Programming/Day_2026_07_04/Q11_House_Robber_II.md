# House Robber II

## Problem Statement
The problem is a variation of the classic House Robber problem. In this version, the houses are arranged in a circular manner, meaning that the first house is connected to the last house. The goal is to find the maximum amount of money that can be stolen from the houses without stealing from adjacent houses. Each house has a certain amount of money, and the thief can only steal from one house at a time. The input is an array of integers representing the amount of money in each house, and the output is the maximum amount of money that can be stolen.

## Approach
The algorithm uses dynamic programming to solve the problem. It first considers the case where the first house is not stolen, and then the case where the first house is stolen. The maximum amount of money that can be stolen is the maximum of these two cases.

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

        // case 1: first house is not stolen
        vector<int> dp1(n);
        dp1[0] = 0;
        dp1[1] = nums[1];
        for (int i = 2; i < n; i++) {
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
        }

        // case 2: first house is stolen
        vector<int> dp2(n);
        dp2[0] = nums[0];
        dp2[1] = nums[0];
        for (int i = 2; i < n; i++) {
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i]);
        }

        return max(dp1[n-1], dp2[n-1]);
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
- The problem can be solved using dynamic programming by considering two cases: the first house is not stolen, and the first house is stolen.
- The time complexity is O(n) because we need to iterate through the array twice.
- The space complexity is O(n) because we need to store the dynamic programming arrays.