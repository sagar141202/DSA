# Coin Change

## Problem Statement
Given a set of coin denominations and a total amount of money, find the fewest number of coins needed to make change for the given amount. The coin denominations are unlimited, and we can use each denomination any number of times. For example, if we have coin denominations of 1, 2, and 5, and we want to make change for 11, the fewest number of coins needed is 3 (5 + 5 + 1). If it's not possible to make change for the given amount, return -1.

## Approach
We will use dynamic programming to solve this problem, building up a table of minimum coin counts for each amount from 0 to the target amount. The algorithm will iterate over each coin denomination and update the table accordingly. The final result will be stored in the last entry of the table.

## Complexity
- Time: O(amount * num_denominations)
- Space: O(amount)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int coinChange(vector<int>& coins, int amount) {
    // Create a table to store the minimum coin count for each amount
    vector<int> dp(amount + 1, INT_MAX);
    dp[0] = 0; // Base case: 0 coins needed to make 0 amount

    // Iterate over each coin denomination
    for (int coin : coins) {
        // Iterate over each amount from the coin denomination to the target amount
        for (int i = coin; i <= amount; i++) {
            // Update the table with the minimum coin count
            dp[i] = min(dp[i], dp[i - coin] + 1);
        }
    }

    // Return the minimum coin count for the target amount, or -1 if not possible
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
- Dynamic programming is useful for solving problems with overlapping subproblems, like the coin change problem.
- The table-based approach allows us to avoid recalculating the same subproblems multiple times, reducing the time complexity.
- The algorithm's correctness relies on the optimal substructure of the problem, where the optimal solution can be constructed from the optimal solutions of its subproblems.