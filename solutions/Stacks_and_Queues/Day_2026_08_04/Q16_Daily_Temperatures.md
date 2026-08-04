# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If a warmer temperature does not occur, the answer is 0. The input list will contain at least one element, and all elements will be integers. For example, given the list `[73, 74, 75, 71, 69, 72, 76, 73]`, the output should be `[1, 1, 4, 2, 1, 1, 0, 0]`.

## Approach
We will use a stack-based approach to keep track of the indices of the temperatures. We iterate through the list, popping elements from the stack when a warmer temperature is found and updating the result list accordingly. The algorithm runs in linear time, making it efficient for large inputs.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> dailyTemperatures(vector<int>& temperatures) {
    int n = temperatures.size();
    vector<int> result(n, 0);
    stack<int> st;
    
    for (int i = 0; i < n; i++) {
        // While the stack is not empty and the current temperature is greater than the temperature at the top of the stack
        while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
            // Get the index of the top element
            int idx = st.top();
            st.pop();
            // Update the result list
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
- Use a stack to keep track of the indices of the elements that do not have a warmer temperature yet.
- Iterate through the list, updating the result list whenever a warmer temperature is found.
- The algorithm runs in linear time, making it efficient for large inputs.