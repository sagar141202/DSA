# Coin Change

## Problem Statement
The coin change problem is a classic problem in dynamic programming. Given a set of coins with different denominations and a total amount of money, find the minimum number of coins needed to make change for the given amount. The problem has the following constraints: the amount of money is a non-negative integer, and the denominations of the coins are positive integers. For example, if we have coins with denominations 1, 2, and 5, and we want to make change for 11, the minimum number of coins needed is 3 (5 + 5 + 1).

## Approach
The algorithm uses dynamic programming to build up a table of minimum coin counts for each amount from 0 to the target amount. It iterates over each coin denomination and updates the table accordingly. The final result is stored in the last entry of the table. The key insight is to use a bottom-up approach, starting from the smallest amounts and gradually building up to the target amount.

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
                // Update the table with the minimum coin count
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        // Return the minimum coin count for the target amount
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
- The coin change problem can be solved using dynamic programming with a time complexity of O(n*m), where n is the target amount and m is the number of coin denominations.
- The space complexity is O(n), where n is the target amount.
- The key insight is to use a bottom-up approach, starting from the smallest amounts and gradually building up to the target amount.