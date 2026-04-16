# Coin Change

## Problem Statement
Given a set of coins with denominations of 1, 5, 10, 25, and an amount of money, find the number of ways to make change for that amount using the given coins. The amount of money is a non-negative integer, and the number of ways to make change should be calculated modulo 1e9 + 7 to avoid overflow. For example, if the amount is 5, there are 2 ways to make change: using a single coin of denomination 5, or using 5 coins of denomination 1.

## Approach
The problem can be solved using dynamic programming, where we build up a table of solutions to subproblems and use them to solve the original problem. We initialize a table dp of size amount + 1, where dp[i] represents the number of ways to make change for amount i. We then fill up the table by iterating over each coin and updating dp[i] accordingly.

## Complexity
- Time: O(amount * number_of_coins)
- Space: O(amount)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int coinChange(int amount, vector<int>& coins) {
    // Initialize dp table with size amount + 1
    vector<int> dp(amount + 1, 0);
    // Base case: there is 1 way to make change for amount 0 (using no coins)
    dp[0] = 1;
    // Iterate over each coin
    for (int coin : coins) {
        // Iterate over each amount from coin to amount
        for (int i = coin; i <= amount; i++) {
            // Update dp[i] by adding the number of ways to make change for amount i - coin
            dp[i] = (dp[i] + dp[i - coin]) % (int)(1e9 + 7);
        }
    }
    // Return the number of ways to make change for the given amount
    return dp[amount];
}

int main() {
    int amount = 5;
    vector<int> coins = {1, 5};
    cout << coinChange(amount, coins) << endl;
    return 0;
}
```

## Test Cases
```
Input: amount = 5, coins = [1, 5]
Output: 2
Input: amount = 10, coins = [1, 5, 10]
Output: 4
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The dp table should be initialized with a size that is sufficient to store the solutions to all subproblems.
- The base case should be handled carefully to ensure that the dp table is filled up correctly.