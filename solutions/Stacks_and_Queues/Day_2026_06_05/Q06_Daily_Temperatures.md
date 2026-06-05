# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If a warmer temperature does not occur, the answer is 0. The input list will contain at least one element, and all elements will be integers between 30 and 100 (inclusive). For example, given the temperatures [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0].

## Approach
We can use a stack to store the indices of the temperatures. We iterate over the temperatures, and for each temperature, we pop all the indices from the stack where the temperature at that index is less than the current temperature. The difference between the current index and the popped index is the number of days until a warmer temperature occurs. We then push the current index onto the stack.

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
- Use a stack to store the indices of the temperatures to efficiently find the next warmer temperature.
- Iterate over the temperatures and pop all indices from the stack where the temperature is less than the current temperature to calculate the number of days until a warmer temperature occurs.
- Push the current index onto the stack to keep track of the temperatures that have not yet found a warmer temperature.