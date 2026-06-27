# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob.

## Approach
The problem can be solved using dynamic programming by maintaining two arrays: one for the maximum amount that can be robbed up to each house and another for the maximum amount that can be robbed up to the previous house. The maximum amount that can be robbed at each house is the maximum of the amount that can be robbed up to the previous house and the sum of the amount in the current house and the amount that can be robbed up to the house two positions before.

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
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total money you can rob = 1 + 3 = 4.
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- The `dp` array is used to store the maximum amount that can be robbed up to each house.
- The final answer is stored in the last element of the `dp` array.