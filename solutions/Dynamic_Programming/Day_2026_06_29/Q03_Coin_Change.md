# Coin Change

## Problem Statement
The coin change problem is a classic dynamic programming problem where we are given a set of coins with different denominations and a total amount of money. The goal is to find the minimum number of coins required to make change for the given amount. We are allowed to use each coin any number of times. For example, if we have coins with denominations 1, 2, and 5, and we want to make change for 11, the minimum number of coins required would be 3 (5 + 5 + 1). The problem has the following constraints: 1 <= coin denominations <= 100, 1 <= total amount <= 10000.

## Approach
We will use dynamic programming to solve this problem by building up a table of minimum coin counts for each amount from 1 to the total amount. The algorithm works by iterating over each coin and updating the minimum count for each amount. We will use a bottom-up approach to fill up the table.

## Complexity
- Time: O(n*m)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int coinChange(vector<int>& coins, int amount) {
    // Create a table to store the minimum number of coins for each amount
    vector<int> dp(amount + 1, INT_MAX);
    dp[0] = 0; // Base case: 0 coins are needed to make 0 amount

    // Iterate over each coin
    for (int coin : coins) {
        // Iterate over each amount from the coin value to the total amount
        for (int i = coin; i <= amount; i++) {
            // Update the minimum count for the current amount
            dp[i] = min(dp[i], dp[i - coin] + 1);
        }
    }

    // Return the minimum number of coins for the total amount
    return dp[amount] == INT_MAX ? -1 : dp[amount];
}
```

## Test Cases
```
Input: coins = [1, 2, 5], amount = 11
Output: 3
Input: coins = [2], amount = 3
Output: -1
```

## Key Takeaways
- The coin change problem can be solved using dynamic programming by building up a table of minimum coin counts for each amount.
- The time complexity of the solution is O(n*m), where n is the total amount and m is the number of coins.
- The space complexity of the solution is O(n), where n is the total amount.