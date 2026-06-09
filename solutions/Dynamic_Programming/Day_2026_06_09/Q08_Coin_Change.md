# Coin Change

## Problem Statement
Given a set of coins with different denominations and an amount of money, find the fewest number of coins needed to make change for the given amount. The coin denominations are 1, 5, 10, 25, and the amount of money can range from 1 to 100. If it's not possible to make change for the given amount, return -1. For example, if the amount is 11, the fewest number of coins needed is 2 (10 + 1). If the amount is 3, the fewest number of coins needed is 3 (1 + 1 + 1).

## Approach
The algorithm uses dynamic programming to build up a table of minimum coin counts for each amount from 1 to the given amount. The intuition is to consider each coin denomination and update the minimum count for each amount accordingly. The base case is when the amount is 0, in which case the minimum count is 0.

## Complexity
- Time: O(n*m)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int coinChange(int amount) {
    // Create a table to store the minimum coin counts
    int coins[] = {1, 5, 10, 25};
    int n = sizeof(coins) / sizeof(coins[0]);
    int dp[amount + 1];
    // Initialize the table with infinity
    for (int i = 0; i <= amount; i++) {
        dp[i] = INT_MAX;
    }
    // Base case: 0 coins needed to make 0 amount
    dp[0] = 0;
    // Fill up the table
    for (int i = 1; i <= amount; i++) {
        for (int j = 0; j < n; j++) {
            if (coins[j] <= i) {
                dp[i] = min(dp[i], dp[i - coins[j]] + 1);
            }
        }
    }
    // If it's not possible to make change, return -1
    if (dp[amount] == INT_MAX) {
        return -1;
    }
    return dp[amount];
}
```

## Test Cases
```
Input: amount = 11
Output: 2
Input: amount = 3
Output: 3
Input: amount = 0
Output: 0
```

## Key Takeaways
- The dynamic programming approach allows us to avoid redundant calculations and solve the problem efficiently.
- The time complexity is O(n*m), where n is the amount and m is the number of coin denominations.
- The space complexity is O(n), where n is the amount.