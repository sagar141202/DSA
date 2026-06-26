# Coin Change

## Problem Statement
The coin change problem is a classic problem in dynamic programming where we are given a set of coins with different denominations and a total amount of money. The goal is to find the minimum number of coins needed to make up the given amount. We can use each coin any number of times. For example, if we have coins with denominations 1, 2, and 5, and we want to make 11, the minimum number of coins needed is 3 (5 + 5 + 1). The constraints are that the amount of money is a non-negative integer and the denominations of the coins are positive integers.

## Approach
The algorithm uses dynamic programming to build up a table of minimum coin counts for each amount from 0 to the target amount. It iterates over each coin and updates the minimum count for each amount. The intuition is to use the minimum count for the amount without the current coin and the minimum count for the amount minus the current coin's denomination plus one.

## Complexity
- Time: O(amount * num_coins)
- Space: O(amount)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int coinChange(vector<int>& coins, int amount) {
    // Create a table to store the minimum coin count for each amount
    vector<int> dp(amount + 1, INT_MAX);
    dp[0] = 0; // Base case: 0 coins needed to make 0 amount

    // Iterate over each coin
    for (int coin : coins) {
        // Iterate over each amount from the coin's denomination to the target amount
        for (int i = coin; i <= amount; i++) {
            // Update the minimum count for the current amount
            dp[i] = min(dp[i], dp[i - coin] + 1);
        }
    }

    // Return the minimum coin count for the target amount
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
- The dynamic programming approach is useful for solving problems with overlapping subproblems.
- The time complexity is proportional to the amount and the number of coins.
- The space complexity is proportional to the amount.