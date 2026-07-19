# Climbing Stairs

## Problem Statement
You are climbing a staircase with 'n' steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has 1 to 'n' steps, and you start at the 0th step. For example, if there are 4 steps, you can climb the stairs in the following ways: [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2]. 

## Approach
This problem can be solved using dynamic programming by breaking it down into smaller subproblems, where each subproblem represents the number of ways to climb 'i' steps. We can then build up the solution by using the results from these subproblems. The idea is to maintain an array where the ith index stores the number of ways to climb 'i' steps.

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
        
        // Create a dp array to store the number of ways to climb 'i' steps
        vector<int> dp(n + 1);
        
        // Base cases
        dp[1] = 1;
        dp[2] = 2;
        
        // Fill up the dp array
        for (int i = 3; i <= n; i++) {
            // For each step 'i', the number of ways to climb is the sum of the number of ways to climb 'i-1' and 'i-2' steps
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // Return the number of ways to climb 'n' steps
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
- The problem can be broken down into smaller subproblems, where each subproblem represents the number of ways to climb 'i' steps.
- Dynamic programming is used to store the results of these subproblems and build up the solution.
- The time complexity is O(n) because we only need to fill up the dp array once, and the space complexity is also O(n) because we need to store the dp array.