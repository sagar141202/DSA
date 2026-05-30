# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed using these bars. The width of each bar is 1 unit, and the height is given by the corresponding value in the array. The rectangle must be formed by selecting a contiguous subset of the bars and drawing a horizontal line at a height that is less than or equal to the height of each bar in the subset.

## Approach
We will use a stack-based approach to solve this problem. The idea is to maintain a stack of indices of the bars and keep track of the maximum area that can be formed with each bar as the smallest bar. We will iterate through the array, pushing indices onto the stack when the current bar is higher than the bar at the top of the stack, and popping indices when the current bar is lower.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    stack<int> s;
    int maxArea = 0;
    int index = 0;
    while (index < heights.size()) {
        if (s.empty() || heights[index] >= heights[s.top()]) {
            s.push(index);
            index++;
        } else {
            int top = s.top();
            s.pop();
            int width = s.empty() ? index : index - s.top() - 1;
            maxArea = max(maxArea, heights[top] * width);
        }
    }
    while (!s.empty()) {
        int top = s.top();
        s.pop();
        int width = s.empty() ? index : index - s.top() - 1;
        maxArea = max(maxArea, heights[top] * width);
    }
    return maxArea;
}

int main() {
    vector<int> heights = {2, 1, 5, 6, 2, 3};
    cout << largestRectangleArea(heights) << endl;
    return 0;
}
```

## Test Cases
```
Input: [2, 1, 5, 6, 2, 3]
Output: 10
```

## Key Takeaways
- The stack is used to store the indices of the bars, not the heights themselves.
- The width of the rectangle is calculated based on the position of the top of the stack and the current index.
- The maximum area is updated at each step when a bar is popped from the stack.