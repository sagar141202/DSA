# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The histogram is drawn such that the x-axis is horizontal and the y-axis is vertical. The area of a rectangle is calculated as the product of its width and height.

## Approach
We will use a stack-based approach to solve this problem, where we maintain a stack of indices of the histogram bars. We iterate through the histogram, pushing indices onto the stack when the current bar is higher than the bar at the top of the stack, and popping indices when the current bar is lower.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    int n = heights.size();
    vector<int> left(n), right(n);
    stack<int> s;

    // find the index of the first bar to the left that is lower than the current bar
    for (int i = 0; i < n; i++) {
        while (!s.empty() && heights[s.top()] >= heights[i]) {
            s.pop();
        }
        left[i] = s.empty() ? 0 : s.top() + 1;
        s.push(i);
    }

    while (!s.empty()) {
        s.pop();
    }

    // find the index of the first bar to the right that is lower than the current bar
    for (int i = n - 1; i >= 0; i--) {
        while (!s.empty() && heights[s.top()] >= heights[i]) {
            s.pop();
        }
        right[i] = s.empty() ? n - 1 : s.top() - 1;
        s.push(i);
    }

    int maxArea = 0;
    for (int i = 0; i < n; i++) {
        int area = heights[i] * (right[i] - left[i] + 1);
        maxArea = max(maxArea, area);
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
- Use a stack to keep track of the indices of the histogram bars.
- Calculate the area of the rectangle for each bar by multiplying its height with the width, which is the difference between the right and left boundaries.
- Update the maximum area whenever a larger rectangle is found.