# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you start at the 0th step. The function should return the number of distinct ways to climb to the top. For example, if n = 4, there are 5 distinct ways to climb to the top: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
The problem can be solved using dynamic programming by building up a solution from smaller sub-problems. We can create an array where each element represents the number of ways to reach that step. The number of ways to reach a step is the sum of the number of ways to reach the previous step and the step before that.

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
        
        // Initialize an array to store the number of ways to reach each step
        vector<int> dp(n + 1, 0);
        dp[1] = 1;
        dp[2] = 2;
        
        // Fill up the array using the recurrence relation
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // Return the number of ways to reach the top
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
- Dynamic programming is useful for solving problems that have overlapping sub-problems.
- The problem can be solved using a bottom-up approach by filling up an array with the number of ways to reach each step.
- The time complexity of the solution is O(n) and the space complexity is O(n), where n is the number of steps.