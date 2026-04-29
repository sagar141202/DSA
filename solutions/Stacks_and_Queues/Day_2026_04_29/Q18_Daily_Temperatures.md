# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If a warmer temperature does not occur, the answer is 0. For example, given the temperatures [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0]. The temperature list size will be in the range [1, 30000]. The temperature values will be in the range [30, 100].

## Approach
We use a stack to keep track of the indices of the temperatures. We iterate through the list of temperatures, and for each temperature, we check if the stack is not empty and the current temperature is greater than the temperature at the top of the stack. If this condition is met, we calculate the difference between the current index and the index at the top of the stack and update the result list. We then pop the top of the stack and repeat the process until the stack is empty or the current temperature is not greater than the temperature at the top of the stack.

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
            // calculate the difference between the current index and the index at the top of the stack
            int index = s.top();
            result[index] = i - index;
            // pop the top of the stack
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
- Iterate through the list of temperatures and update the result list based on the condition.
- The time complexity is O(n) and the space complexity is O(n) due to the use of the stack.