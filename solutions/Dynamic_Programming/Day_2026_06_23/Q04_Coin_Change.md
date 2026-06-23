# Coin Change

## Problem Statement
Given a set of coin denominations and a total amount of money, find the number of ways to make change for the given amount using the available coin denominations. The problem has the following constraints: 
- The coin denominations are positive integers.
- The total amount of money is a positive integer.
- Each coin denomination can be used any number of times.
- The order of the coins does not matter.
For example, if we have coin denominations of 1, 2, and 5, and we want to make change for 5, there are 4 ways to do it: 5, 2+2+1, 2+1+1+1, and 1+1+1+1+1.

## Approach
The problem can be solved using dynamic programming by building up a table of solutions to subproblems. We start with the base case where the amount is 0, and then fill in the table for each coin denomination. The number of ways to make change for a given amount is the sum of the number of ways to make change for the amount without using the current coin denomination and the number of ways to make change for the amount minus the current coin denomination.

## Complexity
- Time: O(n*m)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        // Create a table to store the number of ways to make change for each amount
        vector<int> dp(amount + 1, 0);
        // Base case: there is one way to make change for 0 (use no coins)
        dp[0] = 1;
        // Fill in the table for each coin denomination
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                // The number of ways to make change for the current amount is the sum of the number of ways to make change for the amount without using the current coin and the number of ways to make change for the amount minus the current coin
                dp[i] += dp[i - coin];
            }
        }
        // The number of ways to make change for the given amount is stored in the last entry of the table
        return dp[amount];
    }
};
```

## Test Cases
```
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Input: amount = 3, coins = [1, 2]
Output: 2
```

## Key Takeaways
- The problem can be solved using dynamic programming by building up a table of solutions to subproblems.
- The number of ways to make change for a given amount is the sum of the number of ways to make change for the amount without using the current coin denomination and the number of ways to make change for the amount minus the current coin denomination.
- The time complexity of the solution is O(n*m), where n is the amount and m is the number of coin denominations.