# Coin Change

## Problem Statement
Given a set of coins with different denominations and an amount of money, find the minimum number of coins needed to make change for the given amount. The coin denominations are 1, 2, and 5. The amount of money is a positive integer. For example, if the amount is 11, the minimum number of coins needed is 3 (5 + 5 + 1).

## Approach
The problem can be solved using dynamic programming by building up a table of minimum coin counts for each amount from 1 to the target amount. We iterate through each coin denomination and update the minimum count for each amount. The algorithm has a time complexity of O(n*m), where n is the target amount and m is the number of coin denominations.

## Complexity
- Time: O(n*m)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int coinChange(int coins[], int n, int amount) {
    // Create a table to store the minimum coin counts
    int dp[amount + 1];
    
    // Initialize the table with infinity
    for (int i = 0; i <= amount; i++) {
        dp[i] = INT_MAX;
    }
    
    // Base case: 0 coins needed to make 0 amount
    dp[0] = 0;
    
    // Iterate through each coin denomination
    for (int i = 0; i < n; i++) {
        // Iterate through each amount from the coin denomination to the target amount
        for (int j = coins[i]; j <= amount; j++) {
            // Update the minimum coin count for the current amount
            if (dp[j - coins[i]] != INT_MAX) {
                dp[j] = min(dp[j], dp[j - coins[i]] + 1);
            }
        }
    }
    
    // Return the minimum coin count for the target amount
    return dp[amount] == INT_MAX ? -1 : dp[amount];
}

int main() {
    int coins[] = {1, 2, 5};
    int n = sizeof(coins) / sizeof(coins[0]);
    int amount = 11;
    cout << coinChange(coins, n, amount);
    return 0;
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
- Dynamic programming can be used to solve problems with overlapping subproblems.
- The coin change problem has a time complexity of O(n*m), where n is the target amount and m is the number of coin denominations.
- The space complexity is O(n), where n is the target amount.