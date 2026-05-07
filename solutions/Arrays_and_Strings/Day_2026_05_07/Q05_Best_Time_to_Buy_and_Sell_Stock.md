# Best Time to Buy and Sell Stock

## Problem Statement
You are given an array of integers representing the daily stock prices. The goal is to find the best time to buy and sell a stock to maximize the profit. You can only buy and sell the stock once, and you cannot sell the stock before buying it. The array is guaranteed to have at least one element. For example, if the input array is [7, 1, 5, 3, 6, 4], the maximum profit that can be achieved is 5 (buy on day 2 and sell on day 5).

## Approach
The solution involves iterating through the array to find the minimum price and the maximum profit that can be achieved. We keep track of the minimum price seen so far and the maximum profit that can be achieved by selling at the current price.

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
        
        // Iterate through the array
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
Input: [7, 1, 5, 3, 6, 4]
Output: 5
Input: [7, 6, 4, 3, 1]
Output: 0
```

## Key Takeaways
- We only need to keep track of the minimum price seen so far to find the maximum profit.
- The maximum profit can be achieved by selling at the current price if it is greater than the minimum price plus the current maximum profit.
- The time complexity is O(n) because we only iterate through the array once.