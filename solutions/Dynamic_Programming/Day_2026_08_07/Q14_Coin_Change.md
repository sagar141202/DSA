# Coin Change

## Problem Statement
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. The coins array may contain duplicate values, and each coin can be used any number of times. For example, if `coins = [1, 2, 5]` and `amount = 11`, then the output should be `3` because `11 = 5 + 5 + 1`.

## Approach
The problem can be solved using dynamic programming by building a table where each cell represents the minimum number of coins needed to make up a certain amount. We start from the base case where the amount is 0 and then fill up the table iteratively. The algorithm iterates over each coin and updates the table accordingly.

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
        dp[0] = 0; // Base case: 0 coins are needed to make up an amount of 0

        // Fill up the table iteratively
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i >= coin && dp[i - coin] != INT_MAX) {
                    dp[i] = min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        // If the minimum number of coins is still INT_MAX, return -1
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
- Dynamic programming is a suitable approach for problems that have overlapping subproblems and optimal substructure.
- The time complexity of the solution is proportional to the product of the amount and the number of coins.
- The space complexity is proportional to the amount, which is used to store the table.