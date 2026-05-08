# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If a warmer temperature does not occur, the answer is 0. The temperature list consists of integers representing the daily temperatures. For example, given the temperature list [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0].

## Approach
The algorithm uses a stack to keep track of the indices of the temperatures. It iterates over the list, pushing the index of the current temperature onto the stack if the stack is empty or the current temperature is not greater than the temperature at the top of the stack. If the current temperature is greater, it pops the top of the stack and calculates the difference in days until a warmer temperature occurs.

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
        // while the stack is not empty and the current temperature is greater than the temperature at the top of the stack
        while (!s.empty() && temperatures[i] > temperatures[s.top()]) {
            int idx = s.top();
            s.pop();
            result[idx] = i - idx;
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
- Use a stack to keep track of the indices of the temperatures.
- Iterate over the list, pushing the index of the current temperature onto the stack if the stack is empty or the current temperature is not greater than the temperature at the top of the stack.
- If the current temperature is greater, pop the top of the stack and calculate the difference in days until a warmer temperature occurs.