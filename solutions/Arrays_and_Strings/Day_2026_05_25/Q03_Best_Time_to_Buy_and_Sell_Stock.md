# Best Time to Buy and Sell Stock

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum possible profit that can be achieved by buying and selling the stock once. The stock can only be sold after it has been bought, and the selling price must be higher than the buying price. The array will contain at least one element, and all elements will be non-negative integers. For example, if the input is [7, 1, 5, 3, 6, 4], the maximum profit that can be achieved is 5 (buy at price 1, sell at price 6).

## Approach
The algorithm uses a single pass through the array to keep track of the minimum price seen so far and the maximum profit that can be achieved. It iterates over the array, updating the minimum price and maximum profit as it finds lower prices and higher profits. This approach ensures that the maximum profit is found in linear time complexity.

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
        
        // Iterate over the array
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
- Use a single pass through the array to keep track of the minimum price and maximum profit.
- Update the minimum price and maximum profit as we iterate over the array.
- The maximum profit is found when the difference between the current price and the minimum price is greater than the current maximum profit.