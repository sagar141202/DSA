# Climbing Stairs

## Problem Statement
You are climbing a staircase. At each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of a staircase with n steps? The staircase has n steps, and you start at the 0th step. The last step is the nth step. For example, if n = 4, there are 5 ways to climb the stairs: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
The approach to solve this problem is to use dynamic programming. We will create an array where each element represents the number of ways to reach that step. We can reach a step from the previous step or the step before that. So, the number of ways to reach a step is the sum of the number of ways to reach the previous step and the step before that.

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
        
        // create an array to store the number of ways to reach each step
        int dp[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        
        // fill up the array
        for (int i = 3; i <= n; i++) {
            // the number of ways to reach a step is the sum of the number of ways to reach the previous step and the step before that
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // return the number of ways to reach the nth step
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
- The problem can be solved using dynamic programming by breaking it down into smaller sub-problems and storing the results of each sub-problem to avoid redundant computation.
- The time complexity of the solution is O(n), where n is the number of steps in the staircase.
- The space complexity of the solution is O(n), where n is the number of steps in the staircase.