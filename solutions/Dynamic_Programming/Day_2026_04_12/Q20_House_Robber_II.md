# House Robber II

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police. The houses are arranged in a circle, meaning the first house is adjacent to the last house.

## Approach
The algorithm uses dynamic programming to solve the problem in two parts: considering the first house and excluding the last house, and excluding the first house and considering the last house. This approach ensures that the circular constraint is handled correctly by breaking the problem into two linear sub-problems.

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
        
        // Rob the first house, don't rob the last house
        int max1 = helper(nums, 0, nums.size() - 2);
        
        // Don't rob the first house, rob the last house
        int max2 = helper(nums, 1, nums.size() - 1);
        
        return max(max1, max2);
    }
    
    int helper(vector<int>& nums, int start, int end) {
        int dp[nums.size()];
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
Input: nums = [0]
Output: 0
```

## Key Takeaways
- The House Robber II problem requires considering the circular arrangement of houses, which can be solved by breaking it down into two linear sub-problems.
- Dynamic programming is used to store the maximum amount that can be robbed up to each house, ensuring that adjacent houses are not robbed.
- The solution has a time complexity of O(n) and a space complexity of O(n), where n is the number of houses.