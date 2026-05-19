# Coin Change

## Problem Statement
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`. The coins can be used any number of times. For example, if `coins = [1, 2, 5]` and `amount = 11`, the output should be `3` because `11 = 5 + 5 + 1`.

## Approach
This problem can be solved using dynamic programming by building up a table of minimum coin counts for each amount from 0 to the target amount. The algorithm iteratively considers each coin and updates the minimum count for each amount. The base case is when the amount is 0, which requires 0 coins.

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
        // Create a table to store the minimum coin count for each amount
        vector<int> dp(amount + 1, INT_MAX);
        dp[0] = 0;  // Base case: 0 coins are needed to make 0 amount

        // Iterate over each coin
        for (int coin : coins) {
            // Iterate over each amount from the coin value to the target amount
            for (int i = coin; i <= amount; i++) {
                // Update the minimum coin count for the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        // Return the minimum coin count for the target amount, or -1 if it's still INT_MAX
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
- Dynamic programming can be used to solve problems that have overlapping subproblems, such as the coin change problem.
- The key to solving the coin change problem is to build up a table of minimum coin counts for each amount, starting from the base case of 0 amount.
- The time complexity of the solution is proportional to the product of the amount and the number of coins, and the space complexity is proportional to the amount.