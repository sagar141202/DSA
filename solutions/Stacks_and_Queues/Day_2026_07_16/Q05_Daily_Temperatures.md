# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If there is no future day with a warmer temperature, the answer is 0. The input list will contain at least one element, and all elements will be integers between 30 and 100, inclusive. For example, given the list of temperatures [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0].

## Approach
The algorithm uses a stack to store indices of temperatures. It iterates over the list of temperatures, pushing indices onto the stack if the current temperature is not greater than the temperature at the top of the stack. If the current temperature is greater, it calculates the difference in days for each index popped from the stack. The intuition is to maintain a stack of indices of temperatures that do not have a warmer temperature yet.

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
- Use a stack to store indices of elements that do not have a warmer temperature yet.
- Iterate over the list of temperatures and push indices onto the stack if the current temperature is not greater than the temperature at the top of the stack.
- If the current temperature is greater, calculate the difference in days for each index popped from the stack.