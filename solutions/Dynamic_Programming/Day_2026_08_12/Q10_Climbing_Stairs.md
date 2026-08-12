# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you start at the 0th step. The problem requires finding the number of unique paths to the nth step, given that you can move either 1 or 2 steps at a time. For example, if there are 4 steps, you can climb the stairs in 5 distinct ways: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
The solution involves using dynamic programming to store the number of ways to reach each step. The number of ways to reach a step is the sum of the number of ways to reach the previous step and the step before that. This approach breaks down the problem into smaller sub-problems and stores their solutions to avoid redundant computation.

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
Input: n = 5
Output: 8
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping sub-problems.
- The space complexity can be optimized to O(1) by only storing the last two elements of the dp array, as only those are needed to compute the next element. 
- The problem can also be solved using matrix exponentiation or Fibonacci series, but dynamic programming provides a straightforward and efficient solution.