# Climbing Stairs

## Problem Statement
You are climbing a staircase with `n` steps, and you can climb either 1 or 2 steps at a time. At each step, you have two choices: to climb 1 step or to climb 2 steps. The problem is to find the total number of distinct ways to climb to the top of the staircase. The input is an integer `n`, representing the number of steps, and the output is an integer representing the total number of distinct ways to climb to the top. For example, if `n = 4`, there are 5 distinct ways to climb to the top: `1+1+1+1`, `1+1+2`, `1+2+1`, `2+1+1`, `2+2`.

## Approach
The problem can be solved using dynamic programming by breaking it down into smaller sub-problems. We can use a bottom-up approach to build up the solution by calculating the number of ways to climb `i` steps for each `i` from 1 to `n`. The number of ways to climb `i` steps is the sum of the number of ways to climb `i-1` steps and `i-2` steps.

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
        if (n <= 2) return n;
        
        // initialize dp array
        vector<int> dp(n + 1);
        dp[1] = 1;
        dp[2] = 2;
        
        // fill up dp array
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // return the result
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
- The problem can be broken down into smaller sub-problems using dynamic programming.
- The time complexity can be reduced to O(n) by using a bottom-up approach.
- The space complexity can be reduced to O(n) by using a dynamic programming array of size `n+1`.