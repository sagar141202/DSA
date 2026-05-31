# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob.

## Approach
The problem can be solved using dynamic programming by maintaining two arrays, one for the maximum amount that can be robbed up to each house and another for the maximum amount that can be robbed up to the previous house. The algorithm iterates through the array, updating these values based on the maximum amount that can be robbed at each step.

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

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9), and rob house 5 (money = 1).
             Total money you can rob = 2 + 9 + 1 = 12.
```

## Key Takeaways
- The dynamic programming approach allows for efficient computation of the maximum amount that can be robbed.
- The use of a single array `dp` to store the maximum amount that can be robbed up to each house simplifies the solution and reduces space complexity.
- The time complexity of the solution is linear, making it efficient for large inputs.