# Best Time to Buy and Sell Stock

## Problem Statement
You are given an array of integers representing the daily stock prices. The goal is to find the maximum possible profit that can be achieved by buying and selling the stock once. The stock can only be bought before it is sold, and the profit is calculated as the difference between the selling price and the buying price. For example, if the input array is [7, 1, 5, 3, 6, 4], the maximum possible profit is 5 (buy on day 2 and sell on day 5).

## Approach
The approach is to iterate through the array and keep track of the minimum price seen so far and the maximum profit that can be achieved. We initialize the minimum price to the first element of the array and the maximum profit to 0. Then, we iterate through the rest of the array, updating the minimum price and the maximum profit as we go.

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
- We only need to keep track of the minimum price seen so far and the maximum profit that can be achieved.
- We can solve this problem in a single pass through the array, making the time complexity O(n).
- The space complexity is O(1) because we only use a constant amount of space to store the minimum price and the maximum profit.