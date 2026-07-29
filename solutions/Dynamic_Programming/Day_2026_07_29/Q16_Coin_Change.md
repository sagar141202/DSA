# Coin Change

## Problem Statement
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`. The coins can be used any number of times. For example, if `coins = [1, 2, 5]` and `amount = 11`, the output should be `3` because `11 = 5 + 5 + 1`. If `amount = 3` and `coins = [2]`, the output should be `-1` because it's impossible to make `3` with coins of denomination `2`.

## Approach
The problem can be solved using dynamic programming by building up a table of minimum coins needed for each amount from `1` to the target `amount`. We initialize the table with a value greater than the maximum possible number of coins and then fill it up by trying all possible coin denominations for each amount. The base case is when the amount is `0`, which requires `0` coins.

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
        dp[0] = 0; // Base case: 0 coins for amount 0

        // Fill up the table
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i - coin >= 0) {
                    dp[i] = min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        // Return the result
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
- Use dynamic programming to build up a table of minimum coins needed for each amount.
- Initialize the table with a large value and fill it up by trying all possible coin denominations.
- The base case is when the amount is `0`, which requires `0` coins.