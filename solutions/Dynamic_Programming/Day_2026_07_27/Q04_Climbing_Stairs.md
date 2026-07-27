# Climbing Stairs

## Problem Statement
You are climbing a staircase with `n` steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has `n` steps, and you start at the 0th step. The task is to find the total number of ways to reach the `n`th step.

## Approach
This problem can be solved using dynamic programming by breaking it down into smaller sub-problems, where each sub-problem represents the number of ways to reach a specific step. The solution to the larger problem can be constructed from the solutions of the sub-problems.

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
            // For each step, the number of ways to reach it is the sum of the ways to reach the previous two steps
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        // The answer is the number of ways to reach the nth step
        return dp[n];
    }
};
```

## Test Cases
```
Input: n = 4
Output: 5
Explanation: There are five ways to climb four steps:
1. 1 step + 1 step + 1 step + 1 step
2. 1 step + 1 step + 2 steps
3. 1 step + 2 steps + 1 step
4. 2 steps + 1 step + 1 step
5. 2 steps + 2 steps
```

## Key Takeaways
- The problem can be broken down into smaller sub-problems, which is a key characteristic of dynamic programming problems.
- The solution to the larger problem can be constructed from the solutions of the sub-problems, which is another key aspect of dynamic programming.
- The use of a dp array to store the solutions to the sub-problems helps avoid redundant computation and improves the efficiency of the solution.