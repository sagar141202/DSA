# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob.

## Approach
The problem can be solved by using dynamic programming to keep track of the maximum amount of money that can be robbed up to each house. We can either rob the current house or not, and choose the option that gives the maximum amount of money. The base cases are when there are no houses or only one house.

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
        
        // dp[i] represents the maximum amount of money that can be robbed up to the ith house
        vector<int> dp(n);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        
        // for each house from the 2nd to the nth
        for (int i = 2; i < n; i++) {
            // we can either rob the current house or not
            // if we rob the current house, we cannot rob the previous house
            // if we do not rob the current house, we can rob the previous house
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
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total money you can rob = 1 + 3 = 4.
```

## Key Takeaways
- The problem can be solved by using dynamic programming to keep track of the maximum amount of money that can be robbed up to each house.
- We need to consider the base cases when there are no houses or only one house.
- The time complexity is O(n) and the space complexity is O(n), where n is the number of houses.