# Coin Change

## Problem Statement
Given a set of coin denominations and a total amount, find the fewest number of coins needed to make change for the given amount. If it's impossible to make change, return -1. The coin denominations are non-negative integers and the total amount is a non-negative integer. For example, given coin denominations [1, 2, 5] and total amount 11, the fewest number of coins needed is 3 (11 = 5 + 5 + 1).

## Approach
We use dynamic programming to solve this problem by building up a table of minimum coins needed for each amount from 0 to the total amount. The algorithm iterates through each coin denomination and updates the minimum coins needed for each amount. The base case is when the amount is 0, which requires 0 coins.

## Complexity
- Time: O(amount * num_denominations)
- Space: O(amount)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // Create a table to store the minimum coins needed for each amount
        vector<int> dp(amount + 1, INT_MAX);
        dp[0] = 0; // Base case: 0 coins needed for amount 0

        // Iterate through each coin denomination
        for (int coin : coins) {
            // Iterate through each amount from the coin denomination to the total amount
            for (int i = coin; i <= amount; i++) {
                // Update the minimum coins needed for the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        // Return the minimum coins needed for the total amount, or -1 if impossible
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
- Dynamic programming can be used to solve problems with overlapping subproblems, such as the coin change problem.
- The key to dynamic programming is to identify the base case and the recurrence relation, and to use a table to store the solutions to subproblems.
- The time complexity of dynamic programming solutions is often O(n * m), where n is the size of the input and m is the number of subproblems.