# Coin Change

## Problem Statement
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`. The coins array may contain duplicate values, and each coin can be used any number of times. For example, given `coins = [1, 2, 5]` and `amount = 11`, the output should be `3` because `11 = 5 + 5 + 1`.

## Approach
We will use dynamic programming to solve this problem by building up a table where each cell represents the minimum number of coins needed to make up a certain amount. We iterate over each coin and update the table accordingly. The final result will be stored in the last cell of the table.

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
        // Create a table to store the minimum number of coins needed for each amount
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0; // Base case: 0 coins needed to make up 0 amount

        // Iterate over each coin
        for (int coin : coins) {
            // Iterate over each amount from the coin value to the target amount
            for (int i = coin; i <= amount; i++) {
                // Update the table with the minimum number of coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        // Return the result, or -1 if the amount cannot be made up
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
- Use dynamic programming to build up a table of minimum coin counts for each amount.
- Iterate over each coin and update the table to ensure the minimum count is always stored.
- Handle the base case where 0 coins are needed to make up 0 amount.