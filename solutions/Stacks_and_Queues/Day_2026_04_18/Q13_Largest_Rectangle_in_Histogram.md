# Largest Rectangle in Histogram

## Problem Statement
The problem requires finding the area of the largest rectangle that can be formed using the bars of a histogram. The histogram is represented as an array of integers, where each integer represents the height of a bar. The width of each bar is 1 unit. The task is to find the maximum area of the rectangle that can be formed using these bars. For example, given the histogram [2, 1, 5, 6, 2, 3], the maximum area of the rectangle that can be formed is 10 units.

## Approach
The algorithm uses a stack to keep track of the indices of the bars. It iterates over the histogram and pushes the indices of the bars onto the stack if the current bar is higher than the bar at the top of the stack. If the current bar is lower than the bar at the top of the stack, it calculates the area of the rectangle that can be formed using the bar at the top of the stack as the smallest bar.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    // Initialize the stack and the maximum area
    stack<int> s;
    int maxArea = 0;
    int n = heights.size();
    
    // Iterate over the histogram
    for (int i = 0; i <= n; i++) {
        // If the stack is empty or the current bar is higher than the bar at the top of the stack, push the index onto the stack
        while (!s.empty() && (i == n || heights[s.top()] >= heights[i])) {
            // Calculate the area of the rectangle that can be formed using the bar at the top of the stack as the smallest bar
            int height = heights[s.top()];
            s.pop();
            int width = s.empty() ? i : i - s.top() - 1;
            maxArea = max(maxArea, height * width);
        }
        // Push the index onto the stack
        s.push(i);
    }
    return maxArea;
}
```

## Test Cases
```
Input: [2, 1, 5, 6, 2, 3]
Output: 10
```

## Key Takeaways
- Use a stack to keep track of the indices of the bars in the histogram.
- Calculate the area of the rectangle that can be formed using the bar at the top of the stack as the smallest bar when the current bar is lower than the bar at the top of the stack.
- The maximum area of the rectangle that can be formed is updated at each step.