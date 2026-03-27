# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If a warmer temperature does not occur, the answer is 0. For example, given the temperatures [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0]. The temperature list will contain at least one element, and all elements will be integers between 30 and 100.

## Approach
We use a stack-based approach to solve this problem, where we maintain a stack of indices of the temperature list. We iterate through the list and pop elements from the stack when we find a warmer temperature. The algorithm calculates the difference in days between the current index and the index at the top of the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> dailyTemperatures(vector<int>& temperatures) {
    // Initialize result vector with zeros
    vector<int> result(temperatures.size(), 0);
    // Initialize stack to store indices
    stack<int> s;
    
    // Iterate through the temperatures list
    for (int i = 0; i < temperatures.size(); i++) {
        // While the stack is not empty and the current temperature is greater than the temperature at the top of the stack
        while (!s.empty() && temperatures[i] > temperatures[s.top()]) {
            // Calculate the difference in days and update the result vector
            int index = s.top();
            result[index] = i - index;
            // Pop the index from the stack
            s.pop();
        }
        // Push the current index to the stack
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
- Use a stack to store indices of the temperature list.
- Iterate through the list and pop elements from the stack when a warmer temperature is found.
- Calculate the difference in days between the current index and the index at the top of the stack.