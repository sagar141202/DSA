# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
Given an array of integers representing the prices of a stock on different days, find the maximum profit that can be achieved by buying and selling the stock with a cooldown period of one day after each sale. The cooldown period means that after selling the stock, you cannot buy it again on the next day. The problem has the following constraints: 1 <= prices.length <= 5000, and 0 <= prices[i] <= 1000. For example, if the input is [1, 2, 3, 0, 2], the output should be 3, which is achieved by buying on day 0, selling on day 2, and then buying on day 4 and selling on day 4.

## Approach
The problem can be solved using dynamic programming by maintaining three variables: buy, sell, and cooldown. The buy variable represents the maximum profit after buying the stock, the sell variable represents the maximum profit after selling the stock, and the cooldown variable represents the maximum profit after the cooldown period. We update these variables iteratively based on the current price.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n < 2) {
            return 0;
        }
        
        // Initialize variables for the first day
        int buy = -prices[0];
        int sell = 0;
        int cooldown = 0;
        
        for (int i = 1; i < n; i++) {
            // Update the maximum profit after buying the stock
            int newBuy = max(buy, cooldown - prices[i]);
            // Update the maximum profit after selling the stock
            int newSell = max(sell, buy + prices[i]);
            // Update the maximum profit after the cooldown period
            int newCooldown = max(cooldown, sell);
            
            // Update the variables for the next day
            buy = newBuy;
            sell = newSell;
            cooldown = newCooldown;
        }
        
        // Return the maximum profit after the last day
        return sell;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 0, 2]
Output: 3
Input: [1]
Output: 0
```

## Key Takeaways
- We use dynamic programming to solve the problem efficiently by avoiding redundant computations.
- The buy, sell, and cooldown variables are updated iteratively based on the current price to track the maximum profit.
- The final result is the maximum profit after the last day, which is stored in the sell variable.