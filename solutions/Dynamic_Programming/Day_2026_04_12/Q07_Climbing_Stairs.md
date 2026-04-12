# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you start at the 0th step. The function should return the number of distinct ways to climb the staircase. For example, if n = 4, there are 5 distinct ways to climb the staircase: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
This problem can be solved using dynamic programming by breaking it down into smaller subproblems and storing the results of each subproblem to avoid redundant calculations. The idea is to maintain an array where the ith index represents the number of ways to reach the ith step. We can reach the ith step from either the (i-1)th step or the (i-2)th step.

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

        // Initialize an array to store the number of ways to reach each step
        vector<int> ways(n + 1, 0);
        ways[1] = 1;
        ways[2] = 2;

        // Fill up the array using dynamic programming
        for (int i = 3; i <= n; i++) {
            // We can reach the ith step from either the (i-1)th step or the (i-2)th step
            ways[i] = ways[i - 1] + ways[i - 2];
        }

        return ways[n];
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
- The dynamic programming approach is particularly useful for problems that have overlapping subproblems.
- The time complexity of the solution is O(n), where n is the number of steps in the staircase, because we need to fill up an array of size n. The space complexity is also O(n) because we need to store the number of ways to reach each step.