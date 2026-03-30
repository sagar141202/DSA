# Best Time to Buy and Sell Stock

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum possible profit that can be achieved by buying and selling the stock once. The constraint is that you must buy the stock before selling it. For example, if the input array is [7, 1, 5, 3, 6, 4], the maximum profit that can be achieved is 5 (buy at price 1 and sell at price 6). If the input array is [7, 6, 4, 3, 1], the maximum profit is 0, as it's not possible to achieve a profit by buying and selling the stock.

## Approach
The approach is to iterate through the array, keeping track of the minimum price encountered so far and the maximum profit that can be achieved. We update the minimum price and maximum profit as we iterate through the array. This approach has a linear time complexity, making it efficient for large inputs.

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
- We only need to keep track of the minimum price encountered so far to find the maximum profit.
- The maximum profit is updated only when we find a price that can give us a higher profit than the current maximum profit.
- This problem can be solved in linear time complexity, making it efficient for large inputs.