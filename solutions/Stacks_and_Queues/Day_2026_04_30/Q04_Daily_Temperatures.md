# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If a warmer temperature does not occur, the answer is 0. The temperature list consists of integers ranging from 30 to 100. The length of the temperature list is in the range [1, 30000]. For example, given the temperature list [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0].

## Approach
We can use a stack-based approach to solve this problem, where we store the indices of the temperatures in a stack. We iterate over the list of temperatures, and for each temperature, we pop all the indices from the stack where the temperature at that index is less than the current temperature. The difference between the current index and the popped index is the number of days until a warmer temperature occurs.

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
        // pop all indices from the stack where the temperature is less than the current temperature
        while (!st.empty() && temperatures[st.top()] < temperatures[i]) {
            int idx = st.top();
            st.pop();
            result[idx] = i - idx;
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
- Iterate over the list of temperatures and pop the indices from the stack where the temperature is less than the current temperature.
- Calculate the number of days until a warmer temperature occurs by subtracting the popped index from the current index.