# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob.

## Approach
The problem can be solved using dynamic programming by maintaining two arrays, one for the maximum amount that can be robbed up to each house and another for the maximum amount that can be robbed up to the previous house. The maximum amount at each house is the maximum of the amount at the current house plus the amount at the house two positions before, or the amount at the previous house.

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
        if (nums.empty()) return 0;
        if (nums.size() == 1) return nums[0];
        
        vector<int> dp(nums.size());
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        
        for (int i = 2; i < nums.size(); i++) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        
        return dp.back();
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
- Dynamic programming can be used to solve problems with overlapping subproblems.
- The House Robber problem has a time complexity of O(n) and a space complexity of O(n), where n is the number of houses.
- The problem can be optimized to use O(1) space by only keeping track of the previous two houses.