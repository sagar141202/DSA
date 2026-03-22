# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If there is no future day with a warmer temperature, the answer is 0. For example, given the temperature list [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0]. The temperature list will contain at least one element, and all elements will be integers between 30 and 100.

## Approach
We can solve this problem using a stack data structure, where we store the indices of the temperatures. We iterate over the list of temperatures and pop the stack whenever we find a temperature that is greater than the temperature at the top of the stack. The difference between the current index and the popped index is the number of days until a warmer temperature occurs.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> dailyTemperatures(vector<int>& temperatures) {
    // Initialize a stack to store the indices of the temperatures
    stack<int> st;
    // Initialize a vector to store the result
    vector<int> result(temperatures.size(), 0);
    
    // Iterate over the list of temperatures
    for (int i = 0; i < temperatures.size(); i++) {
        // While the stack is not empty and the current temperature is greater than the temperature at the top of the stack
        while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
            // Pop the top of the stack and calculate the number of days until a warmer temperature occurs
            int index = st.top();
            st.pop();
            result[index] = i - index;
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
- Use a stack to store the indices of the temperatures.
- Iterate over the list of temperatures and pop the stack whenever a warmer temperature is found.
- Calculate the number of days until a warmer temperature occurs by subtracting the popped index from the current index.