# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The function should take an integer n as input and return the number of distinct ways to climb n stairs. For example, if n = 4, there are 5 ways to climb: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, and 2+2.

## Approach
The problem can be solved using dynamic programming, where we build up a solution by breaking it down into smaller sub-problems. We can use an array to store the number of ways to climb i stairs. The number of ways to climb i stairs is the sum of the number of ways to climb i-1 stairs and i-2 stairs.

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
        
        // initialize array to store number of ways to climb i stairs
        vector<int> dp(n + 1, 0);
        dp[1] = 1;
        dp[2] = 2;
        
        // fill up the array
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // return the number of ways to climb n stairs
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
- The problem can be broken down into smaller sub-problems and solved using dynamic programming.
- The time complexity is O(n) because we need to fill up the array of size n.
- The space complexity is O(n) because we need to store the array of size n.