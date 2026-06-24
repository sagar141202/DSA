# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you start at the 0th step. The function should return the number of distinct ways to climb to the top. For example, if n = 4, there are 5 distinct ways to climb to the top: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
We can solve this problem using dynamic programming by maintaining an array where each element represents the number of ways to climb to that step. The number of ways to climb to a step is the sum of the number of ways to climb to the previous step and the step before that. This approach allows us to avoid redundant calculations and solve the problem efficiently.

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
        // Base cases: there is 1 way to climb 0 steps and 1 way to climb 1 step
        if (n == 0 || n == 1) {
            return 1;
        }
        
        // Initialize an array to store the number of ways to climb to each step
        vector<int> dp(n + 1);
        dp[0] = 1;
        dp[1] = 1;
        
        // Calculate the number of ways to climb to each step from 2 to n
        for (int i = 2; i <= n; i++) {
            // The number of ways to climb to a step is the sum of the number of ways to climb to the previous step and the step before that
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // Return the number of ways to climb to the top of the staircase
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
- The problem can be solved using dynamic programming to avoid redundant calculations.
- The number of ways to climb to a step is the sum of the number of ways to climb to the previous step and the step before that.
- The time complexity of the solution is O(n), and the space complexity is O(n), where n is the number of steps in the staircase.