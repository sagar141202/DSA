# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If a warmer temperature does not occur, the answer is 0. The input list will contain at least one element, and all elements will be integers between 30 and 100. For example, given the list [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0].

## Approach
We use a stack to keep track of the indices of the temperatures. We iterate over the list of temperatures, and for each temperature, we pop all the indices from the stack where the temperature at that index is less than the current temperature. We then push the current index onto the stack. This way, for each day, we can find the number of days until a warmer temperature occurs by subtracting the popped index from the current index.

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
        // pop all indices where temperature is less than current temperature
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
- Use a stack to keep track of indices where a warmer temperature has not been found yet.
- Iterate over the list of temperatures, popping indices where the temperature is less than the current temperature.
- Calculate the number of days until a warmer temperature occurs by subtracting the popped index from the current index.