# Climbing Stairs

## Problem Statement
You are climbing a staircase. It takes `n` steps to reach to the top. At each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? The function should take an integer `n` as input and return the number of distinct ways to climb to the top. For example, if `n = 4`, the distinct ways to climb to the top are: `[1,1,1,1]`, `[1,1,2]`, `[1,2,1]`, `[2,1,1]`, `[2,2]`. So, the function should return `5` for `n = 4`. The input `n` will be in the range `[1, 45]`.

## Approach
The problem can be solved using dynamic programming by storing the number of ways to climb `i` steps in an array `dp` and using it to calculate the number of ways to climb `i+1` and `i+2` steps. The base cases are when `n` is 1 or 2.

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
        
        // Fill dp array
        for (int i = 3; i <= n; i++) {
            // For each step, we can either come from the previous step or the step before that
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
- The `dp` array is used to store the solutions to subproblems so that they can be reused instead of recalculated.
- The time complexity is linear because we are filling the `dp` array in a single pass.