# Coin Change

## Problem Statement
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If it's impossible to make up the amount, return `-1`. The coins can be used multiple times. For example, given `coins = [1, 2, 5]` and `amount = 11`, the output should be `3` because `11 = 5 + 5 + 1`.

## Approach
The problem can be solved using dynamic programming by building up a table of minimum coin counts for each amount from 0 to the target amount. We initialize a table with a size of `amount + 1` and fill it up iteratively. For each coin, we update the minimum count of coins needed for each amount.

## Complexity
- Time: O(amount * coins.size())
- Space: O(amount)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // Create a table to store the minimum number of coins for each amount
        vector<int> dp(amount + 1, INT_MAX);
        dp[0] = 0; // Base case: 0 coins are needed to make up an amount of 0

        // Iterate over each coin
        for (int coin : coins) {
            // Iterate over each amount from the coin value to the target amount
            for (int i = coin; i <= amount; i++) {
                // Update the minimum count of coins needed for the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        // Return the minimum number of coins needed for the target amount, or -1 if it's impossible
        return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
};
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
- The dynamic programming approach allows us to avoid redundant calculations and solve the problem efficiently.
- The time complexity is O(amount * coins.size()) because we iterate over each coin and each amount.
- The space complexity is O(amount) because we need to store the minimum number of coins for each amount in the table.