# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If there is no future day with a warmer temperature, the answer is 0. For example, given the temperatures [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0]. The temperature list size will be in the range [1, 30000]. The temperature values will be in the range [30, 100].

## Approach
We will use a stack-based approach to keep track of the indices of the temperatures. We iterate through the list of temperatures, and for each temperature, we pop the stack until we find a temperature that is greater than the current one or the stack is empty. The difference between the current index and the index at the top of the stack is the number of days until a warmer temperature occurs.

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
        // pop the stack until we find a temperature that is greater than the current one
        while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
            int idx = st.top();
            st.pop();
            result[idx] = i - idx;
        }
        // push the current index to the stack
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
- Use a stack to keep track of the indices of the temperatures.
- Iterate through the list of temperatures and pop the stack until we find a temperature that is greater than the current one.
- The difference between the current index and the index at the top of the stack is the number of days until a warmer temperature occurs.