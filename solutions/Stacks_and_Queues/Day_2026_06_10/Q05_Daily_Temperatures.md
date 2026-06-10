# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If there is no future day with a warmer temperature, the answer is 0. The input list will contain at least one element, and all elements will be integers in the range [30, 100]. For example, given the temperatures [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0].

## Approach
We use a stack to keep track of the indices of the temperatures. We iterate through the list, and for each temperature, we pop all the indices from the stack where the temperature at that index is less than the current temperature. We then push the current index onto the stack. This way, the stack always contains the indices of the temperatures that do not have a warmer temperature to their right yet.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> dailyTemperatures(vector<int>& temperatures) {
    stack<int> s;
    vector<int> result(temperatures.size(), 0);
    
    for (int i = 0; i < temperatures.size(); i++) {
        // pop all indices from the stack where the temperature is less than the current temperature
        while (!s.empty() && temperatures[s.top()] < temperatures[i]) {
            int index = s.top();
            s.pop();
            result[index] = i - index;
        }
        // push the current index onto the stack
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
- Use a stack to keep track of the indices of the temperatures that do not have a warmer temperature to their right yet.
- Pop all indices from the stack where the temperature is less than the current temperature, and update the result accordingly.
- Push the current index onto the stack to keep track of it for future iterations.