# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed using these bars. The width of each bar is 1 unit, and the height is given by the corresponding value in the array. The rectangle must be formed using consecutive bars, and its height is determined by the smallest bar within the selected range.

## Approach
The algorithm uses a stack to keep track of the indices of the bars. It iterates through the array, pushing indices onto the stack when the current bar is higher than the bar at the top of the stack, and popping indices when the current bar is lower. The area of the rectangle formed by each popped bar is calculated and compared to the maximum area found so far.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    int n = heights.size();
    stack<int> s;
    int maxArea = 0;
    
    for (int i = 0; i <= n; i++) {
        // push index onto stack if current bar is higher than bar at top of stack
        while (!s.empty() && (i == n || heights[s.top()] >= heights[i])) {
            int height = heights[s.top()];
            s.pop();
            int width = s.empty() ? i : i - s.top() - 1;
            maxArea = max(maxArea, height * width);
        }
        s.push(i);
    }
    return maxArea;
}
```

## Test Cases
```
Input: heights = [2,1,5,6,2,3]
Output: 10
Input: heights = [2,4]
Output: 2
```

## Key Takeaways
- Use a stack to keep track of the indices of the bars.
- Calculate the area of the rectangle formed by each popped bar.
- Keep track of the maximum area found so far.