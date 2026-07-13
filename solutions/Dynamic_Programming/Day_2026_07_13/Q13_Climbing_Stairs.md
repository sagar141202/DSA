# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The function should take an integer n as input, representing the number of steps in the staircase, and return the number of distinct ways to climb to the top. For example, if n = 4, there are 5 distinct ways to climb to the top: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.

## Approach
The problem can be solved using dynamic programming, where we build up a solution by breaking down the problem into smaller sub-problems and storing the results of these sub-problems to avoid redundant computation. We will use a bottom-up approach to fill up a table with the number of ways to climb i steps.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        vector<int> dp(n + 1);
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
Input: n = 5
Output: 8
```

## Key Takeaways
- The problem can be broken down into smaller sub-problems, where the number of ways to climb i steps depends on the number of ways to climb i-1 and i-2 steps.
- Dynamic programming is used to store the results of these sub-problems and avoid redundant computation.
- The time complexity of the solution is O(n), where n is the number of steps, and the space complexity is O(n) for storing the dp table.