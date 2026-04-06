# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If there is no future day with a warmer temperature, the answer is 0. The temperature values are non-negative integers. For example, given the list of temperatures `[73, 74, 75, 71, 69, 72, 76, 73]`, the output should be `[1, 1, 4, 2, 1, 1, 0, 0]`.

## Approach
We will use a stack-based approach to solve this problem, where we store the indices of the temperatures in the stack. We iterate through the list of temperatures and pop the stack whenever we encounter a temperature that is greater than the temperature at the top of the stack. The difference between the current index and the popped index is the number of days until a warmer temperature occurs.

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
        // Pop the stack whenever we encounter a temperature that is greater than the temperature at the top of the stack
        while (!stack.empty() && temperatures[i] > temperatures[stack.top()]) {
            int index = stack.top();
            stack.pop();
            // Calculate the number of days until a warmer temperature occurs
            result[index] = i - index;
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
- Use a stack to store the indices of the temperatures
- Iterate through the list of temperatures and pop the stack whenever a warmer temperature is encountered
- Calculate the number of days until a warmer temperature occurs by subtracting the popped index from the current index