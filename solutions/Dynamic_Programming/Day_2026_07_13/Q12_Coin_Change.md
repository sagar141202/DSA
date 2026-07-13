# Coin Change

## Problem Statement
Given a set of coins with different denominations and an amount of money, find the minimum number of coins needed to make change for the given amount. The problem has the following constraints: the amount of money is a non-negative integer, and the denominations of the coins are positive integers. For example, if we have coins with denominations 1, 2, and 5, and we want to make change for 11, the minimum number of coins needed is 3 (5 + 5 + 1).

## Approach
The problem can be solved using dynamic programming by building a table that stores the minimum number of coins needed for each amount from 0 to the given amount. We iterate over each coin denomination and update the table accordingly. The final result is stored in the last entry of the table.

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
            // Update the table if using the current coin results in a smaller number of coins
            dp[i] = min(dp[i], dp[i - coin] + 1);
        }
    }

    // Return the minimum number of coins needed for the given amount
    return dp[amount] == INT_MAX ? -1 : dp[amount];
}

int main() {
    vector<int> coins = {1, 2, 5};
    int amount = 11;
    cout << coinChange(coins, amount) << endl; // Output: 3
    return 0;
}
```

## Test Cases
```
Input: coins = [1, 2, 5], amount = 11
Output: 3
Input: coins = [2], amount = 3
Output: -1
Input: coins = [1], amount = 0
Output: 0
```

## Key Takeaways
- The problem can be solved using dynamic programming by building a table that stores the minimum number of coins needed for each amount.
- The time complexity is O(amount * num_denominations) because we iterate over each coin denomination and each amount from the coin denomination to the given amount.
- The space complexity is O(amount) because we need to store the minimum number of coins needed for each amount from 0 to the given amount.