# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police. The constraint is 1 <= nums.length <= 10^4 and 0 <= nums[i] <= 10^4.

## Approach
The problem can be solved using dynamic programming by maintaining two variables: one to store the maximum amount that can be robbed up to the current house and the other to store the maximum amount that can be robbed up to the previous house. We iterate through the array, updating these variables based on whether we rob the current house or not.

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
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total money you can rob = 1 + 3 = 4.
```

## Key Takeaways
- We use dynamic programming to solve this problem as it has overlapping subproblems.
- The base cases are when there is only one house or two houses.
- We maintain an array dp where dp[i] represents the maximum amount we can rob up to the ith house.