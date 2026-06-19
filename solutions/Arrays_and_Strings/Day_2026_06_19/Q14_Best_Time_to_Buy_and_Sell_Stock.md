# Best Time to Buy and Sell Stock

## Problem Statement
You are given an array of integers representing the daily stock prices. The task is to find the best time to buy and sell a stock to maximize the profit. You can only buy and sell the stock once, and you cannot sell the stock before buying it. The input array will have at least one element, and all elements will be non-negative integers. For example, given the array [7, 1, 5, 3, 6, 4], the best time to buy the stock is on the second day (price = 1) and sell it on the fifth day (price = 6), which will result in a profit of 5.

## Approach
The algorithm uses a dynamic programming approach to track the minimum price encountered so far and the maximum profit that can be achieved. It iterates through the array, updating the minimum price and maximum profit at each step. The maximum profit is calculated by subtracting the minimum price from the current price.

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
            minPrice = min(minPrice, price);
            
            // Update maximum profit
            maxProfit = max(maxProfit, price - minPrice);
        }
        
        // Return maximum profit
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
- We only need to keep track of the minimum price encountered so far to calculate the maximum profit.
- The maximum profit is updated at each step by subtracting the minimum price from the current price.
- The time complexity is O(n) because we only iterate through the array once, and the space complexity is O(1) because we only use a constant amount of space to store the minimum price and maximum profit.