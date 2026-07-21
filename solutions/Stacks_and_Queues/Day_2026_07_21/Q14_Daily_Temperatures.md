# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If a warmer temperature does not occur, the answer is 0. The input list will contain at least one element, and all elements are integers representing temperatures. For example, given the temperatures [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0].

## Approach
We can use a stack to keep track of the indices of the temperatures. We iterate over the list of temperatures and for each temperature, we pop all the indices from the stack where the temperature at that index is less than the current temperature. The difference between the current index and the index at the top of the stack (after popping) is the number of days until a warmer temperature occurs.

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
        // pop all indices where temperature is less than current temperature
        while (!s.empty() && temperatures[s.top()] < temperatures[i]) {
            int index = s.top();
            s.pop();
            result[index] = i - index;
        }
        // push current index to stack
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
- Use a stack to keep track of indices where a warmer temperature has not occurred yet.
- Pop indices from the stack where the temperature is less than the current temperature and calculate the difference in indices.
- Push the current index to the stack after popping.