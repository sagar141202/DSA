# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the prices of a stock over time. The goal is to find the maximum profit that can be achieved by buying and selling the stock with a cooldown period of one day after each sale. In other words, if you sell the stock on a given day, you cannot buy it again until two days have passed. The prices array will have at least one element, and all elements will be non-negative integers.

## Approach
The solution uses dynamic programming to track the maximum profit at each step, considering whether we are in a state of holding the stock or not. We maintain two variables: one for the maximum profit when holding the stock and another for the maximum profit when not holding the stock.

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
        if (n < 2) return 0;
        
        // Initialize vectors to store maximum profit at each step
        vector<int> hold(n, 0), sold(n, 0), rest(n, 0);
        
        // Base case: hold the stock on the first day
        hold[0] = -prices[0];
        
        // Iterate through the prices array
        for (int i = 1; i < n; i++) {
            // Maximum profit when holding the stock: either hold from previous day or buy on current day
            hold[i] = max(hold[i-1], rest[i-1] - prices[i]);
            
            // Maximum profit when selling the stock: sell on current day if holding from previous day
            sold[i] = hold[i-1] + prices[i];
            
            // Maximum profit when resting: either rest from previous day or sell on previous day
            rest[i] = max(rest[i-1], sold[i-1]);
        }
        
        // Maximum profit is the maximum of rest and sold on the last day
        return max(rest[n-1], sold[n-1]);
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
- Use dynamic programming to track the maximum profit at each step.
- Consider three states: holding the stock, selling the stock, and resting.
- The maximum profit is the maximum of the rest and sold states on the last day.