# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob.

## Approach
The problem can be solved by using dynamic programming to track the maximum amount of money that can be robbed up to each house. We can either choose to rob the current house or not, depending on which option gives us the maximum amount of money. The decision to rob a house depends on the maximum amount of money that can be robbed from the previous houses.

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
        // Base cases
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return nums[0];
        
        // Initialize dp array
        vector<int> dp(nums.size());
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        
        // Fill up the dp array
        for (int i = 2; i < nums.size(); i++) {
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
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total money you can rob = 1 + 3 = 4.
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- The problem can be broken down into smaller subproblems, and the solution to the larger problem can be constructed from the solutions of the subproblems.
- The time complexity of the solution is O(n), where n is the number of houses, and the space complexity is also O(n) due to the use of the dp array.