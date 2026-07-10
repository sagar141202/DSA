# Coin Change

## Problem Statement
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`. The coins can be used any number of times. For example, if `coins = [1, 2, 5]` and `amount = 11`, the output should be `3` because `11 = 5 + 5 + 1`.

## Approach
The problem can be solved using dynamic programming by building up a table of minimum coin counts for each amount from 0 to the target amount. We start with a base case where 0 coins are needed to make 0 amount, and then iteratively fill up the table. The intuition is to try all possible coins for each amount and choose the one that results in the minimum number of coins.

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
        // Create a dp array to store the minimum number of coins for each amount
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0; // base case: 0 coins needed for 0 amount

        // Fill up the dp array
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i >= coin) {
                    // Try using the current coin and update the dp array if necessary
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The key to solving this problem is to build up a table of minimum coin counts for each amount.
- We need to consider all possible coins for each amount and choose the one that results in the minimum number of coins.