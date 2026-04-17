# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you can start from the 0th step. For example, if n = 4, there are 5 ways to climb: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, and 2+2.

## Approach
This problem can be solved using dynamic programming by breaking it down into smaller sub-problems, where each sub-problem represents the number of ways to climb to a particular step. We can use a bottom-up approach to build up the solution.

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
        // Base cases: there's 1 way to climb 0 steps (don't climb) and 1 way to climb 1 step
        if (n <= 1) {
            return 1;
        }
        
        // Create a DP array to store the number of ways to climb to each step
        vector<int> dp(n + 1);
        dp[0] = 1;  // Base case: 1 way to climb 0 steps
        dp[1] = 1;  // Base case: 1 way to climb 1 step
        
        // Fill up the DP array using the recurrence relation
        for (int i = 2; i <= n; i++) {
            // Number of ways to climb to step i is the sum of ways to climb to steps i-1 and i-2
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // The answer is the number of ways to climb to the top step (n)
        return dp[n];
    }
};
```

## Test Cases
```
Input: n = 2
Output: 2
Input: n = 3
Output: 3
Input: n = 4
Output: 5
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping sub-problems.
- The problem can be broken down into smaller sub-problems, and the solution to the larger problem can be constructed from the solutions of the sub-problems.
- The time complexity of the solution is linear (O(n)), and the space complexity is also linear (O(n)).