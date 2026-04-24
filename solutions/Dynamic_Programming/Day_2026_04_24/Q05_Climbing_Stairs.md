# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you start at the 0th step. You can either climb 1 or 2 steps at a time, and you need to find the total number of distinct ways to reach the nth step. For example, if n = 4, there are 5 distinct ways to climb the staircase: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
This problem can be solved using dynamic programming by building up a solution from smaller sub-problems. We will use a bottom-up approach to calculate the number of ways to climb i steps, where i ranges from 1 to n. The number of ways to climb i steps will depend on the number of ways to climb (i-1) and (i-2) steps.

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

        // Initialize an array to store the number of ways to climb i steps
        int dp[n + 1];
        dp[1] = 1;
        dp[2] = 2;

        // Fill up the dp array
        for (int i = 3; i <= n; i++) {
            // The number of ways to climb i steps is the sum of the number of ways to climb (i-1) and (i-2) steps
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        // Return the number of ways to climb n steps
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
- The problem can be broken down into smaller sub-problems, and the solution to the larger problem depends on the solutions to the smaller sub-problems.
- Dynamic programming is an effective approach to solve problems that have overlapping sub-problems.
- The space complexity can be optimized by only storing the number of ways to climb the last two steps, instead of storing the number of ways to climb all steps.