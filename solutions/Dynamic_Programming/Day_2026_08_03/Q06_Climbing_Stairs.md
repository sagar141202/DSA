# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you start at the 0th step. You can climb either 1 or 2 steps at a time. For example, if there are 4 steps, you can climb the stairs in the following ways: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2. The function should return the total number of distinct ways to climb the stairs.

## Approach
The problem can be solved using dynamic programming by breaking it down into smaller subproblems and storing the results of these subproblems to avoid redundant calculations. We can use an array to store the number of ways to climb i steps. The number of ways to climb i steps is the sum of the number of ways to climb i-1 steps and i-2 steps.

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
        
        // initialize array to store the number of ways to climb i steps
        vector<int> dp(n + 1, 0);
        dp[1] = 1;
        dp[2] = 2;
        
        // fill up the array using dynamic programming
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
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
```

## Key Takeaways
- Use dynamic programming to break down the problem into smaller subproblems and store the results of these subproblems.
- Initialize an array to store the number of ways to climb i steps.
- Fill up the array using dynamic programming by calculating the number of ways to climb i steps as the sum of the number of ways to climb i-1 steps and i-2 steps.