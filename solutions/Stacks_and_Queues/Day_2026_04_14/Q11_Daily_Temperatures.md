# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If there is no future day with a warmer temperature, the answer is 0. The temperature values are non-negative integers.

## Approach
We use a stack-based approach to solve this problem, where we store the indices of the temperatures in the stack. We iterate over the list of temperatures and pop the stack whenever we find a temperature that is greater than the temperature at the top of the stack. The difference between the current index and the popped index gives us the number of days until a warmer temperature occurs.

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
        // pop the stack if the current temperature is greater than the temperature at the top of the stack
        while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
            int idx = st.top();
            st.pop();
            result[idx] = i - idx;
        }
        // push the current index onto the stack
        st.push(i);
    }
    return result;
}
```

## Test Cases
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

## Key Takeaways
- Use a stack to store the indices of the temperatures.
- Pop the stack whenever a warmer temperature is found and calculate the difference between the current index and the popped index.
- If there is no future day with a warmer temperature, the answer is 0.