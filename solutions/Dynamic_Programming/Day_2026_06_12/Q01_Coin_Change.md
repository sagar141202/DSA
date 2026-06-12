# Coin Change

## Problem Statement
Given a set of coins with denominations of 1, 2, and 5, find the number of ways to make change for a given amount using these coins. The function should take an integer amount as input and return the number of ways to make change for that amount. For example, if the amount is 5, the function should return 4, because there are 4 ways to make change for 5: 5, 2+2+1, 2+1+1+1, and 1+1+1+1+1. The amount will not exceed 10000.

## Approach
The problem can be solved using dynamic programming, where we build up a table of solutions to subproblems. We start with a base case where the amount is 0, and then fill in the table for each amount from 1 to the given amount. The number of ways to make change for a given amount is the sum of the number of ways to make change for the amount minus each coin denomination.

## Complexity
- Time: O(amount * denominations)
- Space: O(amount)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int coinChange(int amount) {
    int denominations[] = {1, 2, 5};
    int n = sizeof(denominations) / sizeof(denominations[0]);
    vector<int> dp(amount + 1, 0);
    dp[0] = 1; // base case: 1 way to make change for 0 amount

    for (int i = 1; i <= amount; i++) {
        for (int j = 0; j < n; j++) {
            if (i >= denominations[j]) {
                dp[i] += dp[i - denominations[j]];
            }
        }
    }

    return dp[amount];
}
```

## Test Cases
```
Input: 5
Output: 4
Input: 10
Output: 10
```

## Key Takeaways
- The problem can be solved using dynamic programming by building up a table of solutions to subproblems.
- The time complexity is O(amount * denominations) because we need to iterate over each amount and each denomination.
- The space complexity is O(amount) because we need to store the number of ways to make change for each amount.