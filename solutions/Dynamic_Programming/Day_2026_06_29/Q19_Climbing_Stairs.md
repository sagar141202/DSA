# Climbing Stairs

## Problem Statement
You are climbing a stair case with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of a staircase with n steps? The function should take an integer n as input and return the number of distinct ways to climb n stairs. For example, if n = 4, there are 5 distinct ways to climb the stairs: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
The problem can be solved using dynamic programming by building up a solution from smaller sub-problems. We can create an array where each element represents the number of ways to climb to that step. The number of ways to climb to a step is the sum of the number of ways to climb to the previous step and the step before that.

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
        if (n <= 2) return n;
        vector<int> dp(n + 1, 0);
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
};
```

## Test Cases
```
Input: 4
Output: 5
Input: 5
Output: 8
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping sub-problems.
- The problem can be broken down into smaller sub-problems and the solutions to these sub-problems can be stored in an array for later use.
- The time complexity of the solution is O(n) and the space complexity is O(n), where n is the number of steps.