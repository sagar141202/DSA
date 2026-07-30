# Daily Temperatures

## Problem Statement
Given a list of daily temperatures, produce a list that, for each day, tells you how many days you would have to wait until a warmer temperature occurs. If there is no future day with a warmer temperature, the answer is 0. Constraints: The length of temperatures will be in the range [1, 30,000]. Each temperature will be an integer in the range [30, 100].

## Approach
We can use a stack-based approach to solve this problem, where we maintain a stack of indices of the temperatures array. For each temperature, we pop all the indices from the stack where the temperature at that index is less than the current temperature. We then push the current index onto the stack.

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
    stack<int> tempStack;
    
    for (int i = 0; i < n; i++) {
        // While the stack is not empty and the temperature at the top of the stack is less than the current temperature
        while (!tempStack.empty() && temperatures[tempStack.top()] < temperatures[i]) {
            int idx = tempStack.top();
            tempStack.pop();
            result[idx] = i - idx;
        }
        tempStack.push(i);
    }
    
    return result;
}
```

## Test Cases
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

## Key Takeaways
- Use a stack to store indices of the temperatures array to efficiently find the next warmer temperature.
- Iterate through the temperatures array and pop indices from the stack where the temperature is less than the current temperature.
- Calculate the difference in days between the current index and the popped index to get the result.