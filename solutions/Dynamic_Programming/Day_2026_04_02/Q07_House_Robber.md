# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob.

## Approach
The algorithm uses dynamic programming to build up a solution by considering each house as a potential target, while ensuring that no two adjacent houses are robbed. The maximum amount of money that can be robbed up to each house is calculated based on the maximum amount that can be robbed up to the previous house and the house two positions before.

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
        
        // Create a dp array to store the maximum amount of money that can be robbed up to each house
        vector<int> dp(nums.size());
        
        // Base cases
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        
        // Fill up the dp array
        for (int i = 2; i < nums.size(); i++) {
            // For each house, the maximum amount of money that can be robbed is the maximum of the amount that can be robbed up to the previous house
            // and the amount that can be robbed up to the house two positions before plus the amount in the current house
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        
        // The maximum amount of money that can be robbed is stored in the last element of the dp array
        return dp[nums.size() - 1];
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
- The problem can be solved using dynamic programming by considering each house as a potential target.
- The maximum amount of money that can be robbed up to each house is calculated based on the maximum amount that can be robbed up to the previous house and the house two positions before.
- The time complexity is O(n) and the space complexity is O(n), where n is the number of houses.