# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers representing the heights of bars in a histogram, find the largest rectangle that can be formed within the histogram. The width of each bar is 1 unit, and the height of each bar is given by the corresponding element in the array. The task is to find the maximum area of the rectangle that can be formed using the bars of the histogram. For example, given the array [2, 1, 5, 6, 2, 3], the largest rectangle has an area of 10 units.

## Approach
The approach to solve this problem is to use a stack-based solution, where we iterate through the array and push the indices of the bars onto the stack. We then pop the top element from the stack and calculate the area of the rectangle that can be formed using the popped bar as the smallest bar.

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
        // if stack is empty or current bar is higher than the bar at the top of the stack, push the current index
        if (s.empty() || heights[index] >= heights[s.top()]) {
            s.push(index);
            index++;
        } else {
            // if current bar is smaller than the bar at the top of the stack, calculate the area
            int top = s.top();
            s.pop();
            int width = s.empty() ? index : index - s.top() - 1;
            int area = heights[top] * width;
            maxArea = max(maxArea, area);
        }
    }
    
    // calculate the area for the remaining bars in the stack
    while (!s.empty()) {
        int top = s.top();
        s.pop();
        int width = s.empty() ? index : index - s.top() - 1;
        int area = heights[top] * width;
        maxArea = max(maxArea, area);
    }
    
    return maxArea;
}

// example usage
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
Input: [2, 4]
Output: 2
```

## Key Takeaways
- Use a stack to keep track of the indices of the bars in the histogram.
- Calculate the area of the rectangle that can be formed using the popped bar as the smallest bar.
- The time complexity is O(n), where n is the number of bars in the histogram.