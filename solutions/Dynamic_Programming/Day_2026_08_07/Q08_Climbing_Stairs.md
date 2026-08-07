# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you start at the 0th step. You can only climb 1 or 2 steps at a time. For example, if there are 4 steps, you can climb in the following ways: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
The problem can be solved using dynamic programming, where we build up a solution by breaking it down into smaller subproblems. We can use an array to store the number of ways to climb to each step. The number of ways to climb to the current step is the sum of the number of ways to climb to the previous step and the step before that.

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
        // base cases
        if (n == 1) return 1;
        if (n == 2) return 2;
        
        // initialize array to store the number of ways to climb to each step
        vector<int> dp(n + 1, 0);
        dp[1] = 1;
        dp[2] = 2;
        
        // fill up the array
        for (int i = 3; i <= n; i++) {
            // the number of ways to climb to the current step is the sum of the number of ways to climb to the previous step and the step before that
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // return the number of ways to climb to the top of the staircase
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
- The problem can be broken down into smaller subproblems, and the solution to the larger problem can be built up from the solutions to the smaller subproblems.
- Dynamic programming can be used to store the solutions to the smaller subproblems and avoid redundant computation.
- The space complexity can be optimized by only storing the necessary information, in this case, the number of ways to climb to the previous step and the step before that.