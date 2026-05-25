# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Approach
The algorithm uses dynamic programming to track the maximum amount of money that can be robbed up to each house. It considers two cases: robbing the current house or not robbing it. The maximum amount of money that can be robbed is the maximum of these two cases.

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
        // base case: if there are no houses, return 0
        if (nums.empty()) return 0;
        
        // base case: if there is only one house, return the money in that house
        if (nums.size() == 1) return nums[0];
        
        // initialize a dynamic programming array
        vector<int> dp(nums.size());
        
        // the maximum amount of money that can be robbed up to the first house is the money in the first house
        dp[0] = nums[0];
        
        // the maximum amount of money that can be robbed up to the second house is the maximum of the money in the first house and the money in the second house
        dp[1] = max(nums[0], nums[1]);
        
        // for each house from the third house onwards
        for (int i = 2; i < nums.size(); i++) {
            // the maximum amount of money that can be robbed up to the current house is the maximum of the maximum amount of money that can be robbed up to the previous house and the sum of the money in the current house and the maximum amount of money that can be robbed up to the house two positions before the current house
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        
        // the maximum amount of money that can be robbed is the last element in the dynamic programming array
        return dp.back();
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
- The problem can be solved using dynamic programming by tracking the maximum amount of money that can be robbed up to each house.
- The maximum amount of money that can be robbed up to the current house is the maximum of the maximum amount of money that can be robbed up to the previous house and the sum of the money in the current house and the maximum amount of money that can be robbed up to the house two positions before the current house.
- The time complexity of the solution is O(n), where n is the number of houses.