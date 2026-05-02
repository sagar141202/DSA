# Coin Change

## Problem Statement
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`. The coins array may contain duplicate values, and each coin can be used any number of times. For example, if `coins = [1, 2, 5]` and `amount = 11`, then the output should be `3` because `11 = 5 + 5 + 1`.

## Approach
The problem can be solved using dynamic programming by building up a table of minimum coin counts for each amount from 0 to the target amount. We initialize the table with a value of `amount + 1` for all amounts, except for 0 which is 0, and then iterate over each coin and update the table accordingly. This approach ensures that we consider all possible combinations of coins.

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
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0; // Base case: 0 coins are needed to make up an amount of 0

        // Iterate over each coin
        for (int coin : coins) {
            // Iterate over each amount from the coin value to the target amount
            for (int i = coin; i <= amount; i++) {
                // Update the table with the minimum number of coins
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        // Return the minimum number of coins, or -1 if it's not possible
        return dp[amount] > amount ? -1 : dp[amount];
    }
};
```

## Test Cases
```
Input: coins = [1, 2, 5], amount = 11
Output: 3
Input: coins = [2], amount = 3
Output: -1
```

## Key Takeaways
- Dynamic programming is a powerful technique for solving problems that have overlapping subproblems.
- The key to solving the coin change problem is to build up a table of minimum coin counts for each amount.
- The time complexity of the solution is O(amount * coins.size()) because we iterate over each coin and each amount.