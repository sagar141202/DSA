# Climbing Stairs

## Problem Statement
You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? For example, if n = 4, there are 5 ways to climb: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2. The input n will be a positive integer, and you should return the number of distinct ways to climb n steps.

## Approach
This problem can be solved using dynamic programming, where we build up a solution by breaking down the problem into smaller sub-problems. We can climb 1 or 2 steps at a time, so the number of ways to climb n steps is the sum of the number of ways to climb n-1 and n-2 steps.

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
        
        // initialize dp array
        int dp[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        
        // fill up dp array
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
Input: n = 5
Output: 8
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping sub-problems.
- The time complexity of this solution is O(n) because we are filling up a dp array of size n.
- The space complexity of this solution is O(n) because we are using a dp array of size n to store the number of ways to climb i steps.