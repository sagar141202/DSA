# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If there is no future day with a warmer temperature, the answer is 0. For example, given the temperature list `[73, 74, 75, 71, 69, 72, 76, 73]`, the output should be `[1, 1, 4, 2, 1, 1, 0, 0]`. The temperature list will contain at least one element, and all elements will be integers in the range `[30, 100]`.

## Approach
Use a stack to keep track of indices of temperatures. Iterate through the list, popping from the stack when a warmer temperature is found. The difference between the current index and the popped index is the number of days until a warmer temperature. The stack will store indices of temperatures that do not yet have a warmer temperature.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
#include <stack>

vector<int> dailyTemperatures(vector<int>& temperatures) {
    int n = temperatures.size();
    vector<int> result(n, 0);
    stack<int> st;
    
    for (int i = 0; i < n; i++) {
        // While the stack is not empty and the current temperature is greater than the temperature at the top of the stack
        while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
            // Get the index of the top of the stack
            int idx = st.top();
            st.pop();
            // Calculate the number of days until a warmer temperature
            result[idx] = i - idx;
        }
        // Push the current index onto the stack
        st.push(i);
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
- Use a stack to efficiently keep track of indices that do not yet have a warmer temperature.
- When a warmer temperature is found, calculate the difference between the current index and the index at the top of the stack.
- The stack will be empty at the end of the iteration, indicating that all temperatures have a corresponding number of days until a warmer temperature.