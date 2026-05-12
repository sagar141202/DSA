# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If a warmer temperature does not occur, the answer is 0. The temperature list consists of integers representing daily temperatures. For example, given the temperature list [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0]. The temperature on day 0 is 73, and the next warmer temperature is on day 1 with a temperature of 74, so the answer for day 0 is 1.

## Approach
We use a stack-based approach to solve this problem, where we push the index of each temperature onto the stack. When a warmer temperature is encountered, we pop the top of the stack and calculate the difference between the current index and the popped index. This difference represents the number of days until a warmer temperature occurs.

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
        // While the stack is not empty and the current temperature is greater than the temperature at the top of the stack
        while (!s.empty() && temperatures[i] > temperatures[s.top()]) {
            // Pop the top of the stack and calculate the difference between the current index and the popped index
            int idx = s.top();
            s.pop();
            result[idx] = i - idx;
        }
        // Push the current index onto the stack
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
- Use a stack to keep track of the indices of temperatures that do not have a warmer temperature yet.
- When a warmer temperature is encountered, pop the top of the stack and calculate the difference between the current index and the popped index.
- The time complexity is O(n) because each temperature is pushed and popped from the stack exactly once.