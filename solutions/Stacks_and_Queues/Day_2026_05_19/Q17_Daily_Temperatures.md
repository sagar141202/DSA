# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If a warmer temperature does not occur, the answer is 0. The input list will contain at least one element, and all elements will be integers. For example, given the list [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0].

## Approach
The algorithm uses a stack to keep track of the indices of the temperatures. It iterates over the list of temperatures, pushing the index of the current temperature onto the stack if it's not warmer than the temperature at the top of the stack. If it is warmer, it calculates the difference in days between the current index and the index at the top of the stack, and updates the result list accordingly. This process continues until the stack is empty.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> dailyTemperatures(vector<int>& temperatures) {
    // Initialize result vector with zeros
    vector<int> result(temperatures.size(), 0);
    // Initialize stack to store indices
    stack<int> stack;
    
    // Iterate over temperatures
    for (int i = 0; i < temperatures.size(); i++) {
        // While stack is not empty and current temperature is greater than temperature at top of stack
        while (!stack.empty() && temperatures[i] > temperatures[stack.top()]) {
            // Get index from top of stack
            int index = stack.top();
            // Calculate difference in days
            result[index] = i - index;
            // Pop index from stack
            stack.pop();
        }
        // Push current index onto stack
        stack.push(i);
    }
    return result;
}
```

## Test Cases
```
Input: [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

## Key Takeaways
- Use a stack to keep track of indices of temperatures.
- Iterate over temperatures, pushing indices onto stack if current temperature is not warmer than temperature at top of stack.
- Calculate difference in days when a warmer temperature is found, and update result list accordingly.