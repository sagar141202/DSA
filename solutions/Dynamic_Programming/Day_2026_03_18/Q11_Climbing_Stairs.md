# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you start at the 0th step. The function should take an integer n as input and return the number of distinct ways to climb the staircase. For example, if n = 4, there are 5 distinct ways to climb the staircase: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
This problem can be solved using dynamic programming, where we build up a solution by breaking down the problem into smaller subproblems. We use a bottom-up approach to calculate the number of ways to climb i steps. The algorithm is based on the fact that the number of ways to climb i steps is the sum of the number of ways to climb (i-1) steps and (i-2) steps.

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
        
        // Initialize dp array
        vector<int> dp(n + 1, 0);
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
Input: n = 5
Output: 8
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The bottom-up approach is often more efficient than the top-down approach for dynamic programming problems.
- The time complexity of this solution is O(n) because we only need to iterate through the dp array once to fill it up.