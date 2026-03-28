# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob.

## Approach
The algorithm uses dynamic programming to build up a solution by considering each house one by one, choosing the maximum amount that can be robbed up to the current house. The decision to rob or not rob the current house depends on the maximum amount that can be robbed up to the previous house or the house two positions before.

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
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        
        // dp[i] represents the maximum amount that can be robbed up to the i-th house
        vector<int> dp(n);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        
        for (int i = 2; i < n; i++) {
            // For each house, we have two options: rob it or not rob it
            // If we rob it, the maximum amount is the amount in the current house plus the maximum amount up to the house two positions before
            // If we don't rob it, the maximum amount is the same as the maximum amount up to the previous house
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        
        return dp[n-1];
    }
};
```

## Test Cases
```
Input: nums = [1,2,3,1]
Output: 4
Input: nums = [2,7,9,3,1]
Output: 12
```

## Key Takeaways
- The problem can be solved using dynamic programming by building up a solution one house at a time.
- The decision to rob or not rob the current house depends on the maximum amount that can be robbed up to the previous house or the house two positions before.
- The time complexity is O(n) and the space complexity is O(n), where n is the number of houses.