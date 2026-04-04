# Climbing Stairs

## Problem Statement
You are climbing a staircase that has n steps. At each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you start at the 0th step. You can climb either 1 or 2 steps at a time. For example, if n = 4, there are 5 distinct ways to climb the staircase: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2. The function should return the number of distinct ways to climb the staircase.

## Approach
The problem can be solved using dynamic programming by breaking it down into smaller subproblems and storing the results of each subproblem to avoid redundant computation. We can create an array where the ith element represents the number of ways to climb i steps. The number of ways to climb i steps is the sum of the number of ways to climb i-1 steps and i-2 steps.

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
        
        // Create an array to store the number of ways to climb i steps
        vector<int> dp(n + 1, 0);
        dp[1] = 1;
        dp[2] = 2;
        
        // Fill the array using dynamic programming
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // Return the number of ways to climb n steps
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
- The problem can be broken down into smaller subproblems using dynamic programming.
- The number of ways to climb i steps is the sum of the number of ways to climb i-1 steps and i-2 steps.
- The time complexity is O(n) and the space complexity is O(n) due to the use of the dp array.