# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Approach
The problem can be solved using dynamic programming by maintaining two arrays, one for the maximum amount that can be robbed up to each house and another to track whether the current house is robbed or not. However, it can be optimized to use only one array. The idea is to choose the maximum between the amount of money in the current house plus the amount of money that can be robbed up to two houses before, or the amount of money that can be robbed up to the previous house.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
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
- The problem is a classic example of dynamic programming where we break down the problem into smaller subproblems and solve each subproblem only once.
- We can optimize the space complexity from O(n) to O(1) by only keeping track of the previous two houses.