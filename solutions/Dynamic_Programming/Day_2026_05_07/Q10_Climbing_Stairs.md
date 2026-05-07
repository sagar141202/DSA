# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you start at the 0th step. The problem has the following constraints: 1 <= n <= 45. For example, if n = 4, there are 5 distinct ways to climb to the top: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
The problem can be solved using dynamic programming by breaking it down into smaller subproblems and storing the results of each subproblem to avoid redundant calculations. We will use a bottom-up approach to build up the solution. The idea is to calculate the number of ways to climb i steps and store it in an array.

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
        
        // initialize an array to store the number of ways to climb i steps
        vector<int> dp(n + 1, 0);
        dp[1] = 1;
        dp[2] = 2;
        
        // calculate the number of ways to climb i steps
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // return the number of ways to climb n steps
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
- The problem can be broken down into smaller subproblems and solved using dynamic programming.
- The time complexity is O(n) because we are calculating the number of ways to climb i steps for each i from 1 to n.
- The space complexity is O(n) because we are storing the number of ways to climb i steps in an array of size n.