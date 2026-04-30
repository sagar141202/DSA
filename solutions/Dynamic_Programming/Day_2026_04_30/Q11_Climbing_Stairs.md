# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and you can climb either 1 or 2 steps at a time. At each step, you have two options: to climb 1 step or 2 steps. The task is to find the total number of distinct ways to reach the top of the staircase. The input is the total number of steps, and the output is the total number of distinct ways to reach the top.

## Approach
The problem can be solved using dynamic programming by breaking it down into smaller subproblems. We can create a DP array where each element represents the number of ways to reach that step. The number of ways to reach a step is the sum of the number of ways to reach the previous step and the step before that.

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
Input: n = 4
Output: 5
Explanation: There are five ways to climb to the top.
1. 1 step + 1 step + 1 step + 1 step
2. 1 step + 1 step + 2 steps
3. 1 step + 2 steps + 1 step
4. 2 steps + 1 step + 1 step
5. 2 steps + 2 steps
```

## Key Takeaways
- The problem can be broken down into smaller subproblems using dynamic programming.
- The number of ways to reach a step is the sum of the number of ways to reach the previous step and the step before that.
- The time complexity of the solution is O(n) and the space complexity is O(n), where n is the total number of steps.