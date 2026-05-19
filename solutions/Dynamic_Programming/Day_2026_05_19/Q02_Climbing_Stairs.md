# Climbing Stairs

## Problem Statement
You are climbing a staircase. At each step, you can either climb 1 or 2 steps. Given the total number of steps `n`, return the number of distinct ways you can climb to the top of the staircase. The staircase has `n` steps, and you start at the 0th step. You can only climb 1 or 2 steps at a time.

## Approach
The problem can be solved using dynamic programming, where we build up a solution by breaking it down into smaller sub-problems. We create an array `dp` of size `n+1`, where `dp[i]` represents the number of ways to climb `i` steps.

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
        // Base cases: 1 way to climb 0 steps, 1 way to climb 1 step
        if (n == 0 || n == 1) return 1;
        
        // Initialize dp array with base cases
        vector<int> dp(n + 1);
        dp[0] = 1;
        dp[1] = 1;
        
        // Fill up dp array
        for (int i = 2; i <= n; i++) {
            // Number of ways to climb i steps is the sum of ways to climb i-1 and i-2 steps
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // Return the number of ways to climb n steps
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
- The problem can be broken down into smaller sub-problems and solved using dynamic programming.
- The `dp` array is used to store the number of ways to climb each step, and the final answer is stored in `dp[n]`.
- The time complexity is O(n) because we only need to fill up the `dp` array once, and the space complexity is also O(n) because we need to store the `dp` array.