# Coin Change

## Problem Statement
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`. The coins can be used any number of times. For example, if `coins = [1, 2, 5]` and `amount = 11`, the output should be `3` because `11 = 5 + 5 + 1`.

## Approach
We will use dynamic programming to solve this problem by building a table that stores the minimum number of coins needed for each amount from 0 to the given amount. The algorithm iterates over each coin and updates the table accordingly. The base case is when the amount is 0, which requires 0 coins.

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
        vector<int> dp(amount + 1, INT_MAX);
        dp[0] = 0; // Base case: 0 coins needed for amount 0

        // Iterate over each coin
        for (int coin : coins) {
            // Iterate over each amount from the coin value to the given amount
            for (int i = coin; i <= amount; i++) {
                // Update the table with the minimum number of coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        // Return the minimum number of coins needed for the given amount
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The table `dp` is used to store the minimum number of coins needed for each amount, and it is updated iteratively.
- The base case is when the amount is 0, which requires 0 coins.