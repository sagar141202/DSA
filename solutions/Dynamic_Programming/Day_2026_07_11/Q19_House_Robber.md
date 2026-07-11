# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob.

## Approach
The problem can be solved using dynamic programming by maintaining two arrays, `dp1` and `dp2`, where `dp1[i]` represents the maximum amount that can be robbed up to the `i-th` house (including the `i-th` house) and `dp2[i]` represents the maximum amount that can be robbed up to the `i-th` house (excluding the `i-th` house). However, a more optimized approach is to use a single array `dp` where `dp[i]` is the maximum amount of money that can be robbed up to the `i-th` house.

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
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return nums[0];
        
        vector<int> dp(nums.size());
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        
        for (int i = 2; i < nums.size(); i++) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        
        return dp[nums.size() - 1];
    }
};
```

## Test Cases
```
Input: nums = [1,2,3,1]
Output: 4
Input: nums = [1,7,1,5,9,2]
Output: 16
```

## Key Takeaways
- We use dynamic programming to solve this problem efficiently by breaking it down into smaller subproblems and storing the results of these subproblems to avoid redundant computation.
- The `dp` array is used to store the maximum amount of money that can be robbed up to the `i-th` house, which helps in making a decision for the next house. 
- The final result is stored in the last index of the `dp` array.