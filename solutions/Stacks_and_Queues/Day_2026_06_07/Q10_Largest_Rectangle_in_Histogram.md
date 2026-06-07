# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The histogram is drawn such that the x-axis is horizontal and the y-axis is vertical, and the bars are placed from left to right in the order given in the input array. The area of a rectangle is calculated as the product of its width and height. The constraints are: 1 <= heights.length <= 10^5 and 0 <= heights[i] <= 10^5.

## Approach
The algorithm uses a stack to keep track of the indices of the bars. It iterates over the array, pushing the indices of the bars onto the stack if the current bar is higher than or equal to the bar at the top of the stack. If the current bar is lower than the bar at the top of the stack, it calculates the area of the rectangle with the bar at the top of the stack as the smallest bar.

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
        maxArea = max(maxArea, (right[i] - left[i] + 1) * heights[i]);
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
- Calculate the area of the rectangle with the bar at the top of the stack as the smallest bar when a smaller bar is encountered.
- The time complexity is O(n) and the space complexity is O(n) due to the use of the stack.