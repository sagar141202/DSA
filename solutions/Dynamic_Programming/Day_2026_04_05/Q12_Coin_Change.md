# Coin Change

## Problem Statement
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`. The coins can be used any number of times. For example, if `coins = [1, 2, 5]` and `amount = 11`, the output should be `3` because `11 = 5 + 5 + 1`. If `amount = 3` and `coins = [2]`, the output should be `-1` because it's impossible to make up `3` using only coins of denomination `2`.

## Approach
This problem can be solved using dynamic programming, where we build up a table of minimum coin counts for each amount from 0 to the target amount. We iterate through each coin and update the minimum count for each amount. The intuition is to use the minimum count of the previous amounts to calculate the minimum count for the current amount.

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
        // Create a table to store the minimum coin count for each amount
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0; // Base case: 0 coins are needed to make up amount 0

        // Iterate through each coin
        for (int coin : coins) {
            // Iterate through each amount from the coin value to the target amount
            for (int i = coin; i <= amount; i++) {
                // Update the minimum count for the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        // Return the minimum coin count for the target amount, or -1 if it's impossible
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
Input: coins = [1], amount = 0
Output: 0
```

## Key Takeaways
- Dynamic programming is a powerful technique for solving problems that have overlapping subproblems.
- The key to solving this problem is to build up a table of minimum coin counts for each amount, using the minimum count of the previous amounts to calculate the minimum count for the current amount.
- The time complexity of this solution is O(amount * coins.size()), where amount is the target amount and coins.size() is the number of different coin denominations.