# Coin Change

## Problem Statement
Given a set of coins with different denominations and an amount of money, find the fewest number of coins needed to make change for the given amount. The coin denominations are unlimited, and we can use each denomination any number of times. For example, if we have coins of denominations 1, 2, and 5, and we want to make change for 11, the fewest number of coins needed is 3 (5 + 5 + 1).

## Approach
We will use dynamic programming to solve this problem, building up a table of minimum coin counts for each amount from 0 to the target amount. We'll iterate through each coin denomination and update the table accordingly. The final result will be the minimum coin count for the target amount.

## Complexity
- Time: O(amount * num_coins)
- Space: O(amount)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int coinChange(vector<int>& coins, int amount) {
    // Create a table to store the minimum coin count for each amount
    vector<int> dp(amount + 1, INT_MAX);
    dp[0] = 0;  // Base case: 0 coins needed to make 0 amount

    // Iterate through each coin denomination
    for (int coin : coins) {
        // Iterate through each amount from the coin denomination to the target amount
        for (int i = coin; i <= amount; i++) {
            // Update the minimum coin count for the current amount
            dp[i] = min(dp[i], dp[i - coin] + 1);
        }
    }

    // Return the minimum coin count for the target amount
    return dp[amount] == INT_MAX ? -1 : dp[amount];
}

int main() {
    vector<int> coins = {1, 2, 5};
    int amount = 11;
    cout << coinChange(coins, amount) << endl;  // Output: 3
    return 0;
}
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
- Dynamic programming is useful for solving problems with overlapping subproblems and optimal substructure.
- The coin change problem has a time complexity of O(amount * num_coins) and a space complexity of O(amount).
- The solution involves building up a table of minimum coin counts for each amount and updating it iteratively based on the coin denominations.