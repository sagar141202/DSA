# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you start at the 0th step. The task is to find the number of distinct ways to reach the nth step.

## Approach
The problem can be solved using dynamic programming by breaking it down into smaller sub-problems and storing the results of each sub-problem to avoid redundant calculations. We will create a DP array where each element represents the number of ways to reach that step.

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
        if (n == 1) return 1;
        if (n == 2) return 2;
        
        vector<int> dp(n + 1, 0);
        dp[1] = 1;
        dp[2] = 2;
        
        for (int i = 3; i <= n; i++) {
            // for each step, the number of ways to reach it is the sum of the ways to reach the previous two steps
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
- The problem can be broken down into smaller sub-problems, and the results of each sub-problem can be stored to avoid redundant calculations.
- The DP array is used to store the number of ways to reach each step, and the final result is the number of ways to reach the nth step.
- The time complexity is O(n) because we are filling up the DP array of size n, and the space complexity is also O(n) because we are using a DP array of size n.