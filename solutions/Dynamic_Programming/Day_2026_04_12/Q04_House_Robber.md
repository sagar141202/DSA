# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob.

## Approach
The algorithm uses dynamic programming to track the maximum amount of money that can be robbed up to each house. It considers two options: robbing the current house or not robbing it, and chooses the option that results in the maximum amount of money. The base cases are when there are no houses or only one house.

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
        
        // dp[i] represents the maximum amount of money that can be robbed up to the i-th house
        vector<int> dp(n);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        
        for (int i = 2; i < n; i++) {
            // consider two options: rob the current house or not rob it
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
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total money you can rob = 2 + 9 + 1 = 12.
```

## Key Takeaways
- The problem can be solved using dynamic programming by tracking the maximum amount of money that can be robbed up to each house.
- The time complexity is O(n) where n is the number of houses, and the space complexity is also O(n) for storing the dp array.
- The solution can be optimized to use O(1) space by only keeping track of the previous two houses.