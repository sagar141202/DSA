# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you are allowed to climb either 1 or 2 steps at a time. For example, if there are 4 steps, you can climb the staircase in the following ways: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
The problem can be solved using dynamic programming by breaking it down into smaller subproblems and storing the results of each subproblem to avoid redundant calculations. We will create an array dp where dp[i] represents the number of ways to climb i steps. The algorithm will iterate through each step and calculate the number of ways to climb to that step by considering the number of ways to climb to the previous step and the step before that.

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
        // Create a dp array to store the number of ways to climb i steps
        vector<int> dp(n + 1);
        
        // Base cases: there is 1 way to climb 0 steps and 1 way to climb 1 step
        dp[0] = 1;
        dp[1] = 1;
        
        // Calculate the number of ways to climb i steps
        for (int i = 2; i <= n; i++) {
            // The number of ways to climb i steps is the sum of the number of ways to climb i-1 steps and i-2 steps
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
- The problem can be broken down into smaller subproblems, and the results of each subproblem can be stored to avoid redundant calculations.
- The dynamic programming approach can be used to solve problems that have overlapping subproblems and optimal substructure.
- The time complexity of the solution is O(n), where n is the number of steps, and the space complexity is also O(n) due to the dp array.