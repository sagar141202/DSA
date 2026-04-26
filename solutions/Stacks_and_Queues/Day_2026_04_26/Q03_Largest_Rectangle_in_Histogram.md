# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers representing the heights of bars in a histogram, find the largest rectangle that can be formed within the histogram. The width of each bar is 1 unit, and the height is given by the corresponding value in the array. The rectangle must be formed by selecting a contiguous subset of bars and drawing a horizontal line at a height that is less than or equal to the height of each bar in the subset.

## Approach
We can use a stack-based approach to solve this problem, where we maintain a stack of indices of the bars. We iterate through the array, pushing indices onto the stack when the current bar is higher than or equal to the bar at the top of the stack, and popping indices when the current bar is lower. We calculate the area of the rectangle that can be formed with the bar at the top of the stack as the smallest bar.

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

    // Iterate through the array
    for (int i = 0; i <= n; i++) {
        // If the stack is empty or the current bar is higher than the bar at the top of the stack, push the index onto the stack
        while (!s.empty() && (i == n || heights[s.top()] > heights[i])) {
            // Calculate the width of the rectangle
            int width = s.empty() ? i : i - s.top() - 1;
            // Calculate the area of the rectangle
            int area = heights[s.top()] * width;
            // Update the maximum area
            maxArea = max(maxArea, area);
            // Pop the index from the stack
            s.pop();
        }
        // Push the index onto the stack
        s.push(i);
    }

    // Return the maximum area
    return maxArea;
}
```

## Test Cases
```
Input: [2,1,5,6,2,3]
Output: 10
Input: [2,4]
Output: 2
```

## Key Takeaways
- Use a stack to keep track of the indices of the bars.
- Calculate the area of the rectangle that can be formed with the bar at the top of the stack as the smallest bar.
- Update the maximum area whenever a larger rectangle is found.