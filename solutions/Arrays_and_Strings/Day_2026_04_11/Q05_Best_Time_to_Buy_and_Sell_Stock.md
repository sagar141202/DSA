# Best Time to Buy and Sell Stock

## Problem Statement
You are given an array of integers representing the daily stock prices. The task is to find the maximum possible profit that can be achieved by buying and selling the stock once. The constraint is that you must buy the stock before selling it. If no profit can be achieved, return 0. For example, given the prices [7,1,5,3,6,4], the maximum profit that can be achieved is 5 (buy at price 1 and sell at price 6).

## Approach
The algorithm uses a single pass through the array to keep track of the minimum price encountered so far and the maximum profit that can be achieved. The idea is to update the minimum price and maximum profit at each step. This approach ensures that we consider all possible buy and sell combinations.

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
            // Update minimum price
            minPrice = min(minPrice, price);
            // Update maximum profit
            maxProfit = max(maxProfit, price - minPrice);
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
- We only need to keep track of the minimum price encountered so far to find the maximum profit.
- The algorithm has a linear time complexity, making it efficient for large inputs.
- The space complexity is constant, as we only use a fixed amount of space to store the minimum price and maximum profit.