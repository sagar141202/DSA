# Coin Change

## Problem Statement
Given a set of coin denominations and a total amount of money, find the fewest number of coins needed to make change for the given amount. The coin denominations are unlimited, and the amount can be any positive integer. For example, if the coin denominations are 1, 2, and 5, and the total amount is 11, the fewest number of coins needed is 3 (5 + 5 + 1). If it's not possible to make change for the given amount, return -1.

## Approach
The problem can be solved using dynamic programming by building up a table of minimum coin counts for each amount from 1 to the target amount. We initialize the table with a value of infinity for all amounts, except for 0, which is 0. Then, for each coin denomination, we update the table by checking if using the current coin results in a smaller count.

## Complexity
- Time: O(n*m)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // Create a table to store the minimum coin count for each amount
        vector<int> dp(amount + 1, INT_MAX);
        dp[0] = 0; // Base case: 0 coins needed to make 0 amount

        // Iterate over each coin denomination
        for (int coin : coins) {
            // Iterate over each amount from the coin denomination to the target amount
            for (int i = coin; i <= amount; i++) {
                // Update the table if using the current coin results in a smaller count
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        // Return the minimum coin count for the target amount, or -1 if it's not possible
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
- Dynamic programming can be used to solve problems that have overlapping subproblems and optimal substructure.
- The table should be initialized with a value of infinity for all amounts, except for the base case.
- The time complexity is O(n*m), where n is the target amount and m is the number of coin denominations.