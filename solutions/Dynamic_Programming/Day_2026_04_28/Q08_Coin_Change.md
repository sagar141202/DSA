# Coin Change

## Problem Statement
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`. The coins can be used any number of times.

## Approach
The problem can be solved using dynamic programming by building up a table of minimum coin counts for each amount from 0 to the target amount. We initialize the table with a value of 0 for amount 0 and infinity for all other amounts. Then, for each coin, we update the table by checking if using the current coin results in a smaller count.

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
        dp[0] = 0;  // Base case: 0 coins are needed to make up amount 0

        // Iterate over each coin
        for (int coin : coins) {
            // Iterate over each amount from the coin value to the target amount
            for (int i = coin; i <= amount; i++) {
                // Update the table if using the current coin results in a smaller count
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        // Return the minimum number of coins or -1 if it's not possible to make up the amount
        return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
};
```

## Test Cases
```
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
Explanation: It's not possible to make up amount 3 using only coins of denomination 2
```

## Key Takeaways
- The dynamic programming approach allows us to avoid redundant calculations and solve the problem efficiently.
- The time complexity is proportional to the product of the amount and the number of coins.
- The space complexity is proportional to the amount, as we need to store the minimum number of coins for each amount from 0 to the target amount.