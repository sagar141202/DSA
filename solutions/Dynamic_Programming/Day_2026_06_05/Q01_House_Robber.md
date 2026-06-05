# House Robber

## Problem Statement
The House Robber problem is a classic dynamic programming problem where a thief plans to rob houses along a street. Each house has a certain amount of money, and the thief cannot rob two adjacent houses. The goal is to find the maximum amount of money that can be stolen. The problem has the following constraints: there are n houses, each house has a non-negative amount of money, and the thief cannot rob the same house twice. For example, if the input is [1,2,3,1], the output should be 4 (rob house 1 and house 3), and if the input is [2,7,9,3,1], the output should be 12 (rob house 2 and house 4).

## Approach
The algorithm uses dynamic programming to build up a solution by considering each house and deciding whether to rob it or not. The decision is based on the maximum amount of money that can be stolen up to the current house. The approach involves creating a dynamic programming table and filling it up using a bottom-up approach.

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
        
        // Create a dynamic programming table
        vector<int> dp(n);
        
        // Base cases
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        
        // Fill up the dynamic programming table
        for (int i = 2; i < n; i++) {
            // For each house, decide whether to rob it or not
            // If we rob the current house, we cannot rob the previous house
            // So, the maximum amount of money we can steal is the maximum of the following two options:
            // 1. Rob the current house and add the maximum amount of money we can steal up to the house two positions before
            // 2. Do not rob the current house and keep the maximum amount of money we can steal up to the previous house
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        
        // The maximum amount of money we can steal is stored in the last position of the dynamic programming table
        return dp[n-1];
    }
};
```

## Test Cases
```
Input: [1,2,3,1]
Output: 4
Input: [2,7,9,3,1]
Output: 12
```

## Key Takeaways
- The problem can be solved using dynamic programming by building up a solution based on the maximum amount of money that can be stolen up to each house.
- The dynamic programming table is filled up using a bottom-up approach, and the maximum amount of money that can be stolen is stored in the last position of the table.
- The time complexity of the solution is O(n), where n is the number of houses, and the space complexity is also O(n).