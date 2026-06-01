# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If there is no future day with a warmer temperature, the answer is 0. The temperature list consists of integers, and the list size will be in the range [1, 30000]. For example, given the list of temperatures `[73, 74, 75, 71, 69, 72, 76, 73]`, the output should be `[1, 1, 4, 2, 1, 1, 0, 0]`.

## Approach
We can solve this problem using a stack data structure, where we store the indices of the temperatures. We iterate over the list of temperatures and pop the stack whenever we find a temperature that is greater than the temperature at the top of the stack. The difference between the current index and the popped index is the number of days until a warmer temperature occurs.

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
        // pop the stack if the current temperature is greater than the temperature at the top of the stack
        while (!s.empty() && temperatures[i] > temperatures[s.top()]) {
            int index = s.top();
            s.pop();
            result[index] = i - index;
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
Input: [89, 62]
Output: [1, 0]
```

## Key Takeaways
- Use a stack to store the indices of the temperatures.
- Iterate over the list of temperatures and pop the stack whenever a warmer temperature is found.
- The difference between the current index and the popped index is the number of days until a warmer temperature occurs.