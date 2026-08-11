# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If a warmer temperature does not occur, the answer is 0. The temperature list consists of integers, and the size of the list is in the range [1, 30,000]. The temperature values are in the range [30,100]. For example, given the temperature list [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0].

## Approach
We can use a stack-based approach to solve this problem. The idea is to maintain a stack of indices of the temperatures list. For each temperature, we pop all the indices from the stack where the temperature at that index is less than the current temperature. We then push the current index onto the stack. The result for each index is the difference between the current index and the index at the top of the stack.

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
    
    // iterate over the temperatures list
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
- Use a stack to keep track of the indices of the temperatures list.
- Pop all indices from the stack where the temperature is less than the current temperature and update the result list.
- Push the current index onto the stack to maintain the order of the temperatures.