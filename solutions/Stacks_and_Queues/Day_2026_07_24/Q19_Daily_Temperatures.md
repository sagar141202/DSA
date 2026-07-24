# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If there is no future day with a warmer temperature, the answer is 0. The temperature list consists of integers representing the daily temperatures. The size of the input list is in the range [1, 10^5]. The temperature values are in the range [30, 100].

## Approach
We can use a stack-based approach to solve this problem efficiently. The stack will store the indices of the temperatures. We iterate through the list of temperatures, and for each temperature, we pop the stack until we find a temperature that is greater than the current one or the stack is empty. The difference between the current index and the top of the stack gives us the number of days until a warmer temperature occurs.

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
    
    // Initialize an empty stack to store indices
    stack<int> stack;
    
    // Iterate through the list of temperatures
    for (int i = 0; i < temperatures.size(); i++) {
        // While the stack is not empty and the current temperature is greater than the temperature at the top of the stack
        while (!stack.empty() && temperatures[i] > temperatures[stack.top()]) {
            // Pop the top of the stack and calculate the result
            int index = stack.top();
            stack.pop();
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
- Use a stack to store the indices of the temperatures for efficient lookups.
- Iterate through the list of temperatures and pop the stack when a warmer temperature is found.
- Calculate the result by subtracting the index at the top of the stack from the current index.