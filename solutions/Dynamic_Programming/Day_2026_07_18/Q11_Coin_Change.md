# Coin Change

## Problem Statement
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If it's impossible to make up the amount, return `-1`. The coins can be used any number of times. For example, given `coins = [1, 2, 5]` and `amount = 11`, the output should be `3` because `11 = 5 + 5 + 1`. If `amount = 3` and `coins = [2]`, the output should be `-1` because it's impossible to make `3` with coins of denomination `2`.

## Approach
The problem can be solved using dynamic programming by maintaining an array `dp` where `dp[i]` represents the fewest number of coins needed to make up the amount `i`. We initialize `dp[0] = 0` and then fill up the `dp` array iteratively. For each coin, we update the `dp` array to reflect the minimum number of coins needed to make up each amount.

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
        // Create a dp array to store the minimum number of coins needed for each amount
        vector<int> dp(amount + 1, INT_MAX);
        dp[0] = 0; // We need 0 coins to make up the amount 0

        // Iterate over each coin
        for (int coin : coins) {
            // Iterate over each amount from the coin value to the target amount
            for (int i = coin; i <= amount; i++) {
                // Update the dp array to reflect the minimum number of coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        // Return the minimum number of coins needed to make up the target amount
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
```

## Key Takeaways
- Dynamic programming is used to solve the problem by maintaining a `dp` array to store the minimum number of coins needed for each amount.
- The `dp` array is filled up iteratively by considering each coin and updating the `dp` array to reflect the minimum number of coins needed to make up each amount.
- The solution has a time complexity of O(amount * coins.size()) and a space complexity of O(amount).