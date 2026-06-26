# Best Time to Buy and Sell Stock

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum possible profit that can be achieved by buying and selling the stock at most once. The stock can only be sold after it is bought, and the profit is the difference between the selling price and the buying price. The input array will contain at least one element, and all elements will be non-negative integers. For example, if the input array is [7, 1, 5, 3, 6, 4], the maximum possible profit is 5, which can be achieved by buying the stock at price 1 and selling it at price 6.

## Approach
The algorithm uses a dynamic programming approach to find the maximum possible profit. It initializes two variables, min_price and max_profit, to the first element of the array and 0 respectively. Then, it iterates over the array, updating min_price and max_profit at each step. The max_profit is updated if the current profit (current price - min_price) is greater than the max_profit.

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
        // Initialize min_price and max_profit
        int min_price = INT_MAX;
        int max_profit = 0;
        
        // Iterate over the array
        for (int price : prices) {
            // Update min_price
            if (price < min_price) {
                min_price = price;
            }
            // Update max_profit
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
Input: [7, 1, 5, 3, 6, 4]
Output: 5
Input: [7, 6, 4, 3, 1]
Output: 0
```

## Key Takeaways
- The algorithm only needs to iterate over the array once to find the maximum possible profit.
- The min_price variable keeps track of the minimum price seen so far, and the max_profit variable keeps track of the maximum possible profit.
- The time complexity of the algorithm is O(n), where n is the number of elements in the input array.