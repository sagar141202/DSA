# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you start at the 0th step. The problem requires finding the number of ways to reach the nth step, given that you can only climb 1 or 2 steps at a time. For example, if n = 4, there are 5 ways to climb the staircase: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
The problem can be solved using dynamic programming by breaking it down into smaller sub-problems and storing the results of each sub-problem to avoid redundant computation. We can create an array where each element represents the number of ways to reach the corresponding step. The number of ways to reach a step is the sum of the number of ways to reach the previous step and the step before that.

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
        
        // Initialize array to store the number of ways to reach each step
        vector<int> ways(n + 1, 0);
        ways[1] = 1;
        ways[2] = 2;
        
        // Fill up the array using dynamic programming
        for (int i = 3; i <= n; i++) {
            ways[i] = ways[i - 1] + ways[i - 2];
        }
        
        // Return the number of ways to reach the nth step
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
- The problem can be broken down into smaller sub-problems, and the results of each sub-problem can be stored to avoid redundant computation.
- Dynamic programming is a powerful technique for solving problems that have overlapping sub-problems.
- The space complexity can be optimized to O(1) by only storing the last two elements of the array, as each element only depends on the previous two elements.