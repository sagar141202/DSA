# Climbing Stairs

## Problem Statement
You are climbing a staircase. It takes `n` steps to reach to the top. At each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? Given the total number of steps `n`, return the number of distinct ways to climb to the top. For example, if `n = 4`, there are 5 ways to climb: `1+1+1+1`, `1+1+2`, `1+2+1`, `2+1+1`, `2+2`. If `n = 3`, there are 3 ways to climb: `1+1+1`, `1+2`, `2+1`.

## Approach
The problem can be solved using dynamic programming by breaking it down into smaller sub-problems and storing the results of each sub-problem to avoid redundant computation. We can create an array `dp` where `dp[i]` represents the number of ways to climb `i` steps. The number of ways to climb `i` steps is the sum of the number of ways to climb `i-1` steps and `i-2` steps.

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

        // Fill up dp array
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
Input: n = 3
Output: 3
```

## Key Takeaways
- The problem can be broken down into smaller sub-problems and solved using dynamic programming.
- The `dp` array is used to store the results of each sub-problem to avoid redundant computation.
- The final result is stored in `dp[n]`, which represents the number of ways to climb `n` steps.