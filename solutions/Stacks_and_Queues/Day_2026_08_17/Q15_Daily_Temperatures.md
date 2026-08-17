# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If there is no future day with a warmer temperature, the answer is 0. For example, given the temperature list [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0]. The temperature list will contain at least one element, and all elements will be integers between 30 and 100.

## Approach
We use a stack-based approach to keep track of the indices of the temperatures. We iterate over the list, pushing the index to the stack if the temperature is not greater than the temperature at the top of the stack. If the temperature is greater, we pop the stack, calculating the difference in days until a warmer temperature occurs.

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
    stack<int> s;
    
    for (int i = 0; i < n; i++) {
        // if stack is not empty and current temperature is greater than temperature at top of stack
        while (!s.empty() && temperatures[i] > temperatures[s.top()]) {
            // calculate the difference in days until a warmer temperature occurs
            int index = s.top();
            result[index] = i - index;
            s.pop();
        }
        // push the current index to the stack
        s.push(i);
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
- Iterate over the list, pushing the index to the stack if the temperature is not greater than the temperature at the top of the stack.
- If the temperature is greater, pop the stack, calculating the difference in days until a warmer temperature occurs.