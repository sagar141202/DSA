# Best Time to Buy and Sell Stock

## Problem Statement
You are given an array of integers representing the daily stock prices. The task is to find the best time to buy and sell a stock to maximize the profit. You can only buy and sell the stock once, and you must buy the stock before selling it. If no profit can be made, return 0.

## Approach
The algorithm uses a two-pointer approach, iterating through the array to find the minimum price and the maximum profit that can be made. It keeps track of the minimum price seen so far and the maximum profit that can be made.

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
        
        // Iterate through the array to find the minimum price and maximum profit
        for (int price : prices) {
            // Update minimum price
            if (price < minPrice) {
                minPrice = price;
            }
            // Update maximum profit
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
Input: prices = [7,1,5,3,6,4]
Output: 5
Input: prices = [7,6,4,3,1]
Output: 0
```

## Key Takeaways
- Always keep track of the minimum price seen so far to maximize the profit.
- Update the maximum profit whenever a higher profit is possible.
- The time complexity is linear, making the solution efficient for large inputs.