# Best Time to Buy and Sell Stock

## Problem Statement
You are given an array of integers representing the daily stock prices. The task is to find the best time to buy and sell a stock to maximize the profit. You can only buy and sell the stock once, and you must buy the stock before selling it. The stock price may fluctuate, and it's possible that the best time to sell is before the last day. For example, given the prices [7, 1, 5, 3, 6, 4], the best time to buy is on the second day (price = 1) and the best time to sell is on the fifth day (price = 6), resulting in a maximum profit of 5.

## Approach
The algorithm uses a simple iterative approach, iterating through the array to find the maximum difference between two elements where the element representing the selling price is after the element representing the buying price. The idea is to keep track of the minimum price encountered so far and the maximum profit that can be achieved.

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
        // Initialize minimum price and maximum profit
        int minPrice = INT_MAX;
        int maxProfit = 0;
        
        // Iterate through the prices array
        for (int price : prices) {
            // Update minimum price if current price is lower
            if (price < minPrice) {
                minPrice = price;
            }
            // Update maximum profit if difference between current price and minPrice is higher
            else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }
        return maxProfit;
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
- Initialize variables to keep track of the minimum price and maximum profit.
- Iterate through the array to update these variables based on the conditions.
- The maximum profit is achieved when the difference between the selling price and the minimum price encountered so far is maximized.