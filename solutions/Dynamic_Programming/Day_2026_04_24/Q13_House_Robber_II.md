# House Robber II

## Problem Statement
The problem is a variation of the classic House Robber problem. In this version, the houses are arranged in a circle, meaning that the first and last houses are adjacent to each other. The goal is to find the maximum amount of money that can be stolen from the houses without stealing from any two adjacent houses. The input is an array of integers representing the amount of money in each house, and the output is the maximum amount of money that can be stolen.

## Approach
The approach is to use dynamic programming to solve the problem. We will break the problem into two sub-problems: one where we steal from the first house and one where we don't steal from the first house. We will then find the maximum amount of money that can be stolen in each sub-problem and return the maximum of the two.

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
        // Base case: if there are no houses, return 0
        if (nums.size() == 0) return 0;
        // Base case: if there is only one house, return the money in that house
        if (nums.size() == 1) return nums[0];
        // Base case: if there are only two houses, return the maximum money in the two houses
        if (nums.size() == 2) return max(nums[0], nums[1]);
        
        // Create a new array that excludes the first house
        vector<int> excludeFirstHouse(nums.begin() + 1, nums.end());
        // Create a new array that excludes the last house
        vector<int> excludeLastHouse(nums.begin(), nums.end() - 1);
        
        // Recursively find the maximum amount of money that can be stolen
        // in the two sub-problems
        return max(robHelper(excludeFirstHouse), robHelper(excludeLastHouse));
    }
    
    int robHelper(vector<int>& nums) {
        // Create a dynamic programming array to store the maximum amount of money
        // that can be stolen up to each house
        vector<int> dp(nums.size());
        // Base case: the maximum amount of money that can be stolen up to the first house
        // is the money in the first house
        dp[0] = nums[0];
        // Base case: the maximum amount of money that can be stolen up to the second house
        // is the maximum of the money in the first house and the money in the second house
        dp[1] = max(nums[0], nums[1]);
        
        // Fill in the rest of the dynamic programming array
        for (int i = 2; i < nums.size(); i++) {
            // The maximum amount of money that can be stolen up to the current house
            // is the maximum of the maximum amount of money that can be stolen up to the
            // previous house and the sum of the money in the current house and the
            // maximum amount of money that can be stolen up to the house two positions
            // before the current house
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        
        // The maximum amount of money that can be stolen is stored in the last position
        // of the dynamic programming array
        return dp.back();
    }
};
```

## Test Cases
```
Input: [2,3,2]
Output: 3
Input: [1,2,3,1]
Output: 4
Input: [1,2,3]
Output: 3
```

## Key Takeaways
- The problem can be broken down into two sub-problems: one where we steal from the first house and one where we don't steal from the first house.
- Dynamic programming can be used to solve the problem by storing the maximum amount of money that can be stolen up to each house.
- The maximum amount of money that can be stolen is the maximum of the maximum amount of money that can be stolen in the two sub-problems.