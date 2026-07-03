# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you start at the 0th step. You can climb either 1 or 2 steps at a time. For example, if there are 4 steps, you can climb in the following ways: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
The problem can be solved using dynamic programming by breaking it down into smaller sub-problems. We can create a dp array where dp[i] represents the number of ways to reach the ith step. The number of ways to reach the ith step is the sum of the number of ways to reach the (i-1)th and (i-2)th steps.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        // Base cases
        if (n == 1) return 1;
        if (n == 2) return 2;
        
        // Create a dp array
        vector<int> dp(n + 1);
        dp[1] = 1;
        dp[2] = 2;
        
        // Fill up the dp array
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        return dp[n];
    }
};
```

## Test Cases
```
Input: n = 4
Output: 5
```

## Key Takeaways
- We use dynamic programming to break down the problem into smaller sub-problems and store the results in a dp array to avoid redundant calculations.
- The time complexity is O(n) because we need to fill up the dp array of size n.
- The space complexity is O(n) because we need to store the dp array of size n.