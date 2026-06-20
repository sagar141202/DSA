# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If a warmer temperature does not occur, the answer is 0. The input list will contain at least one element, and all elements will be integers between 30 and 100 (inclusive). For example, given the list of temperatures [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0].

## Approach
We will use a stack-based approach to solve this problem. The stack will store the indices of the temperatures. We iterate through the list of temperatures, and for each temperature, we pop all the indices from the stack where the temperature at that index is less than the current temperature. The difference between the current index and the popped index is the number of days until a warmer temperature occurs.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> dailyTemperatures(vector<int>& temperatures) {
    stack<int> st;
    vector<int> result(temperatures.size(), 0);
    
    for (int i = 0; i < temperatures.size(); i++) {
        // pop all indices from the stack where the temperature at that index is less than the current temperature
        while (!st.empty() && temperatures[st.top()] < temperatures[i]) {
            int index = st.top();
            st.pop();
            result[index] = i - index;
        }
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
- Iterate through the list of temperatures and pop all indices from the stack where the temperature at that index is less than the current temperature.
- The difference between the current index and the popped index is the number of days until a warmer temperature occurs.