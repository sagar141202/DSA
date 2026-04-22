# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature. If there is no future day with a warmer temperature, the answer is 0. The input list will contain at least one element, and all elements will be integers between 30 and 100. For example, given the list of temperatures [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0].

## Approach
We can use a stack to keep track of the indices of the temperatures. We iterate through the list, and for each temperature, we pop the stack until we find a temperature that is greater than the current one or the stack is empty. The difference between the current index and the top of the stack is the number of days until a warmer temperature.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> dailyTemperatures(vector<int>& temperatures) {
    // Initialize the result vector with zeros
    vector<int> result(temperatures.size(), 0);
    // Initialize the stack
    stack<int> stack;
    // Iterate through the list of temperatures
    for (int i = 0; i < temperatures.size(); i++) {
        // While the stack is not empty and the current temperature is greater than the temperature at the top of the stack
        while (!stack.empty() && temperatures[i] > temperatures[stack.top()]) {
            // Get the index of the top of the stack
            int index = stack.top();
            // Calculate the number of days until a warmer temperature
            result[index] = i - index;
            // Pop the stack
            stack.pop();
        }
        // Push the current index onto the stack
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
- Use a stack to keep track of the indices of the temperatures.
- Iterate through the list of temperatures and pop the stack until a warmer temperature is found.
- Calculate the number of days until a warmer temperature by subtracting the index of the top of the stack from the current index.