# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and you can either climb 1 or 2 steps at a time. At each step, you have two options: climb 1 step or climb 2 steps. The task is to find the total number of distinct ways to climb to the top of the staircase. The input is an integer n, representing the number of steps in the staircase. The output should be the total number of distinct ways to climb to the top.

## Approach
The problem can be solved using dynamic programming by maintaining an array where each element represents the number of ways to climb to that step. The number of ways to climb to the current step is the sum of the number of ways to climb to the previous step and the step before that. This approach ensures that all possible combinations are considered.

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
        // Create a vector to store the number of ways to climb to each step
        vector<int> dp(n + 1);
        
        // Base cases: there is 1 way to climb 0 steps and 1 way to climb 1 step
        dp[0] = 1;
        if (n >= 1) dp[1] = 1;
        
        // For each step from 2 to n, calculate the number of ways to climb to that step
        for (int i = 2; i <= n; i++) {
            // The number of ways to climb to the current step is the sum of the number of ways to climb to the previous step and the step before that
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // Return the number of ways to climb to the top of the staircase
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
- The problem can be solved using dynamic programming by breaking it down into smaller sub-problems and storing the results of each sub-problem to avoid redundant calculations.
- The time complexity of the solution is O(n), where n is the number of steps in the staircase, because we need to calculate the number of ways to climb to each step.
- The space complexity of the solution is O(n), where n is the number of steps in the staircase, because we need to store the number of ways to climb to each step.