# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If a warmer temperature does not occur, the answer is 0. The temperature list consists of non-negative integers, and the length of the list is in the range [1, 30,000]. For example, given the list of temperatures [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0].

## Approach
The algorithm uses a stack to keep track of the indices of the temperatures. It iterates over the list of temperatures, popping the stack whenever it encounters a temperature that is greater than the temperature at the top of the stack. The difference between the current index and the popped index is the number of days until a warmer temperature occurs. The stack is updated with the current index.

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
            // Pop the top of the stack and update the result
            int index = s.top();
            s.pop();
            result[index] = i - index;
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
- Use a stack to keep track of the indices of the temperatures.
- Iterate over the list of temperatures, updating the stack and result as necessary.
- The time complexity is O(n) because each temperature is pushed and popped from the stack exactly once.