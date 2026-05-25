# Coin Change

## Problem Statement
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. The coins array may contain duplicate values, and each coin can be used any number of times. For example, if `coins = [1, 2, 5]` and `amount = 11`, the output should be `3` because `11 = 5 + 5 + 1`.

## Approach
This problem can be solved using Dynamic Programming by building up a table of minimum coin counts for each amount from 0 to the target amount. The algorithm iterates through each coin and updates the minimum count for each amount. The intuition is to find the minimum number of coins for each amount by considering all possible coin combinations.

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
        // Create a DP table to store the minimum number of coins for each amount
        vector<int> dp(amount + 1, INT_MAX);
        dp[0] = 0; // Base case: 0 coins are needed to make 0 amount

        // Iterate through each coin
        for (int coin : coins) {
            // Iterate through each amount from the coin value to the target amount
            for (int i = coin; i <= amount; i++) {
                // Update the minimum count for the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        // Return the minimum count for the target amount, or -1 if it's still INT_MAX
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
- The Dynamic Programming approach allows us to avoid redundant calculations and find the optimal solution efficiently.
- The time complexity is O(amount * coins.size()) because we iterate through each coin and each amount.
- The space complexity is O(amount) because we need to store the minimum count for each amount in the DP table.