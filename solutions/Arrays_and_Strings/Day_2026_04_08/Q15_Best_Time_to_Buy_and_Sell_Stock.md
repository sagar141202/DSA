# Best Time to Buy and Sell Stock

## Problem Statement
You are given an array of integers representing the daily stock prices. The task is to find the maximum possible profit that can be achieved by buying and selling the stock once. The constraint is that you must buy the stock before selling it. If no profit can be achieved, return 0. For example, given the prices [7, 1, 5, 3, 6, 4], the maximum profit that can be achieved is 5 (buy at price 1 and sell at price 6).

## Approach
The algorithm is based on the concept of finding the minimum price before the maximum price. We initialize two variables, min_price and max_profit, to the first price and 0 respectively. Then we iterate through the array, updating min_price and max_profit whenever we find a lower price or a higher profit.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;
        
        int min_price = prices[0];
        int max_profit = 0;
        
        for (int price : prices) {
            // update min_price if current price is lower
            if (price < min_price) {
                min_price = price;
            }
            // update max_profit if current profit is higher
            else if (price - min_price > max_profit) {
                max_profit = price - min_price;
            }
        }
        
        return max_profit;
    }
};
```

## Test Cases
```
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Input: prices = [7, 6, 4, 3, 1]
Output: 0
```

## Key Takeaways
- Initialize min_price and max_profit to the first price and 0 respectively.
- Iterate through the array, updating min_price and max_profit whenever a lower price or higher profit is found.
- Return max_profit as the result.