# Coin Change

## Problem Statement
Given an integer array `coins` representing different denominations of coins and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`. The coins array may contain duplicate values, and each coin can be used any number of times. For example, given `coins = [1, 2, 5]` and `amount = 11`, the output should be `3` because `11 = 5 + 5 + 1`.

## Approach
The problem can be solved using dynamic programming by building up a table of minimum coin counts for each amount from 0 to the target amount. We initialize the table with a large value, then iteratively update each entry with the minimum of its current value and 1 plus the minimum coin count for the amount minus the current coin.

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
        // Initialize a table to store the minimum coin count for each amount
        vector<int> dp(amount + 1, INT_MAX);
        dp[0] = 0;  // Base case: 0 coins needed to make 0 amount

        // Iterate over each coin
        for (int coin : coins) {
            // Iterate from the coin value to the target amount
            for (int i = coin; i <= amount; i++) {
                // Update the minimum coin count for the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        // Return the minimum coin count for the target amount, or -1 if not possible
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
- Dynamic programming is useful for problems that have overlapping subproblems, like finding the minimum coin count for each amount.
- The time complexity is proportional to the product of the amount and the number of coins.
- The space complexity is proportional to the amount, as we need to store the minimum coin count for each amount.