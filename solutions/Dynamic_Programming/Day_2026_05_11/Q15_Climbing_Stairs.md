# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The function should take an integer n as input, representing the number of steps, and return the number of distinct ways to climb to the top. For example, if n = 4, there are 5 distinct ways to climb to the top: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
The problem can be solved using dynamic programming by building up a solution from smaller subproblems. We can use an array to store the number of ways to climb to each step. The number of ways to climb to a step is the sum of the number of ways to climb to the previous step and the step before that.

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
        
        // initialize array to store number of ways to climb to each step
        vector<int> ways(n + 1, 0);
        ways[1] = 1;
        ways[2] = 2;
        
        // build up solution from smaller subproblems
        for (int i = 3; i <= n; i++) {
            ways[i] = ways[i - 1] + ways[i - 2];
        }
        
        // return number of ways to climb to the top
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
- The problem can be broken down into smaller subproblems and solved using dynamic programming.
- The time complexity is O(n) because we only need to iterate up to n to build up the solution.
- The space complexity is O(n) because we need to store the number of ways to climb to each step in an array.