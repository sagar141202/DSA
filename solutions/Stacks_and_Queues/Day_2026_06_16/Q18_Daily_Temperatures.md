# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells us the number of days until a warmer temperature occurs. If no warmer temperature occurs, the answer is 0. For example, given the temperatures [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0]. The input list will contain at least one element, and all elements are integers.

## Approach
We can solve this problem using a stack data structure to keep track of the indices of the temperatures. We iterate over the list of temperatures, pushing the index of the current temperature onto the stack if it's not warmer than the temperature at the top of the stack. If it is warmer, we calculate the difference in days for the temperatures at the top of the stack and pop them until the stack is empty or the current temperature is not warmer.

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
    stack<int> s;

    for (int i = 0; i < n; i++) {
        // While the stack is not empty and the current temperature is greater than the temperature at the top of the stack
        while (!s.empty() && temperatures[i] > temperatures[s.top()]) {
            int idx = s.top();
            s.pop();
            // Calculate the difference in days
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
Input: [89, 62, 70, 58, 59, 90, 75, 85, 73]
Output: [8, 1, 5, 4, 3, 0, 1, 0, 0]
```

## Key Takeaways
- Use a stack to keep track of the indices of the temperatures.
- Iterate over the list of temperatures, pushing the index of the current temperature onto the stack if it's not warmer than the temperature at the top of the stack.
- Calculate the difference in days for the temperatures at the top of the stack when a warmer temperature is found.