# Paint House

## Problem Statement
There are a row of houses, each house can be painted with three colors: red, blue and green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. The cost of painting each house with a certain color is given. Find the minimum cost to paint all houses.

## Approach
The problem can be solved using dynamic programming by maintaining the minimum cost of painting the current house with each color. We iterate over each house, and for each house, we try painting it with each color and update the minimum cost accordingly. The minimum cost to paint the current house with a certain color is the minimum cost to paint the previous house with a different color plus the cost to paint the current house with the certain color.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        if (costs.empty()) return 0;
        int n = costs.size();
        int red = costs[0][0];
        int blue = costs[0][1];
        int green = costs[0][2];
        
        for (int i = 1; i < n; i++) {
            int newRed = min(blue, green) + costs[i][0];
            int newBlue = min(red, green) + costs[i][1];
            int newGreen = min(red, blue) + costs[i][2];
            red = newRed;
            blue = newBlue;
            green = newGreen;
        }
        
        return min({red, blue, green});
    }
};
```

## Test Cases
```
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
```

## Key Takeaways
- Use dynamic programming to solve the problem by maintaining the minimum cost of painting the current house with each color.
- Iterate over each house, and for each house, try painting it with each color and update the minimum cost accordingly.
- The minimum cost to paint the current house with a certain color is the minimum cost to paint the previous house with a different color plus the cost to paint the current house with the certain color.