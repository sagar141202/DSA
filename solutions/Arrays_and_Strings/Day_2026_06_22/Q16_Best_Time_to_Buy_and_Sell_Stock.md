# Best Time to Buy and Sell Stock

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum possible profit that can be achieved by buying and selling the stock once. The constraint is that you can only sell the stock after buying it. For example, if the input array is [7, 1, 5, 3, 6, 4], the maximum possible profit is 5, which can be achieved by buying the stock at price 1 and selling it at price 6.

## Approach
The algorithm uses a single pass through the array to keep track of the minimum price seen so far and the maximum profit that can be achieved. It iterates over the array, updating the minimum price and maximum profit at each step. The maximum profit is calculated by subtracting the minimum price from the current price.

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
- The algorithm has a linear time complexity, making it efficient for large inputs.
- The space complexity is constant, as only a few variables are used to store the minimum price and maximum profit.
- The solution can be extended to find the maximum profit for multiple buy and sell transactions by using a different approach, such as dynamic programming.