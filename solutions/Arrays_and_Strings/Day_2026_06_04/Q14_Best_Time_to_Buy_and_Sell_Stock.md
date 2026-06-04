# Best Time to Buy and Sell Stock

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum possible profit that can be achieved by buying and selling the stock once. The constraint is that you must buy the stock before selling it. For example, if the input array is [7, 1, 5, 3, 6, 4], the maximum profit that can be achieved is 5, which is obtained by buying the stock at price 1 and selling it at price 6.

## Approach
The algorithm uses a single pass through the array to find the maximum profit. It maintains two variables: the minimum price encountered so far and the maximum profit that can be achieved. The maximum profit is updated whenever a higher profit is found.

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
        
        // Iterate through the array to find the maximum profit
        for (int price : prices) {
            // Update the minimum price
            if (price < minPrice) {
                minPrice = price;
            }
            // Update the maximum profit
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
- The algorithm only needs a single pass through the array to find the maximum profit.
- The space complexity is O(1) because only a constant amount of space is used to store the minimum price and the maximum profit.
- The time complexity is O(n) because each element in the array is visited once.