# Best Time to Buy and Sell Stock

## Problem Statement
You are given an array of integers representing the daily stock prices. The task is to find the maximum possible profit that can be achieved by buying and selling the stock once. The constraint is that you must buy the stock before selling it. For example, given the prices [7, 1, 5, 3, 6, 4], the maximum profit can be achieved by buying at price 1 and selling at price 6, resulting in a profit of 5.

## Approach
The approach to solve this problem is to iterate through the array and keep track of the minimum price encountered so far and the maximum profit that can be achieved. The algorithm iterates through the array, updating the minimum price and maximum profit at each step.

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
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Input: prices = [7, 6, 4, 3, 1]
Output: 0
```

## Key Takeaways
- The problem can be solved in a single pass through the array, making it efficient for large inputs.
- The algorithm uses a constant amount of space, making it suitable for systems with limited memory.
- The time complexity of O(n) makes the algorithm scalable for large inputs.