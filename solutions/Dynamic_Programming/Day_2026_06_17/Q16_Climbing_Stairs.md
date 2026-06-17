# Climbing Stairs

## Problem Statement
You are climbing a staircase with n steps, and at each step, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of the staircase? The staircase has n steps, and you can start from the 0th step. For example, if n = 4, there are 5 ways to climb the stairs: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, and 2+2.

## Approach
The problem can be solved using dynamic programming by building up a solution from smaller sub-problems. We can create an array where each element represents the number of ways to reach that step. The number of ways to reach a step is the sum of the number of ways to reach the previous step and the step before that.

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
        
        // Create an array to store the number of ways to reach each step
        vector<int> dp(n + 1, 0);
        dp[1] = 1;
        dp[2] = 2;
        
        // Fill up the array using dynamic programming
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // The number of ways to reach the top is stored in the last element of the array
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
- The time complexity is linear because we only need to iterate through the array once to fill it up.
- The space complexity is also linear because we need to store the number of ways to reach each step in an array.