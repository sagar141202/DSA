# Coin Change

## Problem Statement
Given a set of coins with different denominations and an amount of money, find the fewest number of coins needed to make change for the given amount. The coin denominations are unlimited, and we can use each denomination any number of times. For example, if we have coin denominations of 1, 2, and 5, and we want to make change for 11, the fewest number of coins we need is 3 (5 + 5 + 1). If it's not possible to make change for the given amount, return -1.

## Approach
We will use dynamic programming to solve this problem by building up a table of minimum coins needed for each amount from 0 to the given amount. The algorithm iterates over each coin denomination and updates the table accordingly. The base case is when the amount is 0, in which case we need 0 coins.

## Complexity
- Time: O(amount * num_denominations)
- Space: O(amount)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int coinChange(vector<int>& coins, int amount) {
    // Create a table to store the minimum number of coins needed for each amount
    vector<int> dp(amount + 1, INT_MAX);
    dp[0] = 0; // Base case: 0 coins needed to make 0 amount

    // Iterate over each coin denomination
    for (int coin : coins) {
        // Iterate over each amount from the coin denomination to the given amount
        for (int i = coin; i <= amount; i++) {
            // Update the table with the minimum number of coins needed
            dp[i] = min(dp[i], dp[i - coin] + 1);
        }
    }

    // Return the minimum number of coins needed for the given amount
    return dp[amount] == INT_MAX ? -1 : dp[amount];
}
```

## Test Cases
```
Input: coins = [1, 2, 5], amount = 11
Output: 3
Input: coins = [2], amount = 3
Output: -1
```

## Key Takeaways
- Dynamic programming is useful for solving problems that have overlapping subproblems.
- The table `dp` is used to store the minimum number of coins needed for each amount, and it's updated iteratively based on the coin denominations.
- If it's not possible to make change for the given amount, the function returns -1, indicated by `INT_MAX` in the `dp` table.