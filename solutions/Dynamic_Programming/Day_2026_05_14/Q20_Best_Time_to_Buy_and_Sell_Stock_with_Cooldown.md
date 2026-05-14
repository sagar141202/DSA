# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the prices of a stock over time. You can buy and sell the stock, but you must wait at least one day after selling before you can buy again. The goal is to find the maximum possible profit. For example, given the prices [1, 2, 3, 0, 2], the maximum profit is 3, which can be achieved by buying at price 1, selling at price 3, and then buying at price 0 and selling at price 2.

## Approach
The problem can be solved using dynamic programming by maintaining three variables: buy, sell, and cooldown. The buy variable represents the maximum profit after buying the stock, the sell variable represents the maximum profit after selling the stock, and the cooldown variable represents the maximum profit after a cooldown day.

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
        
        // Initialize variables to store the maximum profit at each step
        vector<int> buy(n), sell(n), cooldown(n);
        
        // Base case: the maximum profit after buying on the first day is -prices[0]
        buy[0] = -prices[0];
        
        // Base case: the maximum profit after selling on the first day is 0
        sell[0] = 0;
        
        // Base case: the maximum profit after a cooldown day on the first day is 0
        cooldown[0] = 0;
        
        // Fill up the dp arrays
        for (int i = 1; i < n; i++) {
            // The maximum profit after buying on the ith day is the maximum of the maximum profit after buying on the (i-1)th day
            // and the maximum profit after a cooldown day on the (i-1)th day minus the price on the ith day
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            
            // The maximum profit after selling on the ith day is the maximum of the maximum profit after selling on the (i-1)th day
            // and the maximum profit after buying on the (i-1)th day plus the price on the ith day
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            
            // The maximum profit after a cooldown day on the ith day is the maximum of the maximum profit after a cooldown day on the (i-1)th day
            // and the maximum profit after selling on the (i-1)th day
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        // The maximum possible profit is the maximum of the maximum profit after selling on the last day
        // and the maximum profit after a cooldown day on the last day
        return max(sell[n-1], cooldown[n-1]);
    }
};
```

## Test Cases
```
Input: prices = [1, 2, 3, 0, 2]
Output: 3
Input: prices = [1]
Output: 0
```

## Key Takeaways
- Use dynamic programming to solve the problem by maintaining three variables: buy, sell, and cooldown.
- The time complexity of the solution is O(n), where n is the number of days.
- The space complexity of the solution is O(n), where n is the number of days.