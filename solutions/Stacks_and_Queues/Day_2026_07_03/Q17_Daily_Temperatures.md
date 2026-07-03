# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If a warmer temperature does not occur, the answer is 0. The temperature list consists of integers representing daily temperatures, and the output should be a list of integers representing the number of days until a warmer temperature occurs. The input list is non-empty and contains at least one element. For example, given the temperature list [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0].

## Approach
We can solve this problem by using a stack to keep track of the indices of the temperatures. We iterate over the list of temperatures, and for each temperature, we pop the stack until we find a temperature that is greater than the current one or the stack is empty. The difference between the current index and the index at the top of the stack is the number of days until a warmer temperature occurs.

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
        while (!s.empty() && temperatures[i] > temperatures[s.top()]) {
            int index = s.top();
            s.pop();
            result[index] = i - index;
        }
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
- Use a stack to keep track of indices of temperatures.
- Iterate over the list of temperatures and pop the stack until a warmer temperature is found.
- Calculate the difference between the current index and the index at the top of the stack to get the number of days until a warmer temperature occurs.