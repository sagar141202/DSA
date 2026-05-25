# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If there is no future day with a warmer temperature, the answer is 0. For example, given the temperature list [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0]. The temperature list will contain at least one element, and all elements will be integers between 30 and 100.

## Approach
The problem can be solved using a stack data structure. We iterate over the list of temperatures and push the indices of the temperatures onto the stack. If we encounter a temperature that is greater than the temperature at the top of the stack, we calculate the difference in days and pop the top element from the stack. This process continues until the stack is empty or the temperature at the top of the stack is greater than or equal to the current temperature.

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
Input: [30, 60, 90]
Output: [1, 1, 0]
```

## Key Takeaways
- Use a stack to store the indices of the temperatures.
- Iterate over the list of temperatures and compare each temperature with the temperature at the top of the stack.
- If a warmer temperature is found, calculate the difference in days and pop the top element from the stack.