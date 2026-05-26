# House Robber II

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police. This is a circular street, which means the first and the last house are adjacent to each other.

## Approach
The algorithm uses dynamic programming to solve the problem by breaking it into two subproblems: one where the first house is robbed and the last house is not, and another where the first house is not robbed. The maximum of these two subproblems is the answer.

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
        
        // Case 1: Rob the first house
        int max1 = helper(nums, 0, nums.size() - 2);
        
        // Case 2: Do not rob the first house
        int max2 = helper(nums, 1, nums.size() - 1);
        
        return max(max1, max2);
    }
    
    int helper(vector<int>& nums, int start, int end) {
        int dp[start + end + 1];
        dp[start] = nums[start];
        dp[start + 1] = max(nums[start], nums[start + 1]);
        
        for (int i = start + 2; i <= end; i++) {
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);
        }
        
        return dp[end];
    }
};
```

## Test Cases
```
Input: nums = [2,3,2]
Output: 3
Input: nums = [1,2,3,1]
Output: 4
Input: nums = [1,2,3]
Output: 3
```

## Key Takeaways
- The problem can be broken down into two subproblems based on whether the first house is robbed or not.
- Dynamic programming is used to solve each subproblem efficiently.
- The final answer is the maximum of the two subproblems.