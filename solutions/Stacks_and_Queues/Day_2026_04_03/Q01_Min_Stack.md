# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and getMin operations in O(1) time. The getMin operation returns the minimum element in the stack. The stack will contain only non-negative integers. For example, given the sequence of operations: push(5), push(3), push(7), getMin, pop, getMin, the output should be 3, 5. The constraints are: 1 <= x <= 10^5, at most 10^4 operations will be performed, and the stack will not be empty when calling pop or top or getMin.

## Approach
We can use two stacks to solve this problem, one for storing the actual elements and another for storing the minimum elements at each step. This allows us to keep track of the minimum element in O(1) time. We update the min stack whenever we push or pop an element from the main stack.

## Complexity
- Time: O(1)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MinStack {
private:
    stack<int> mainStack;
    stack<int> minStack;

public:
    void push(int x) {
        mainStack.push(x);
        if (minStack.empty() || x <= minStack.top()) {
            minStack.push(x);
        }
    }

    void pop() {
        if (!mainStack.empty()) {
            if (mainStack.top() == minStack.top()) {
                minStack.pop();
            }
            mainStack.pop();
        }
    }

    int top() {
        if (!mainStack.empty()) {
            return mainStack.top();
        }
        return -1; // or throw an exception
    }

    int getMin() {
        if (!minStack.empty()) {
            return minStack.top();
        }
        return -1; // or throw an exception
    }
};

int main() {
    MinStack minStack;
    minStack.push(5);
    minStack.push(3);
    minStack.push(7);
    cout << minStack.getMin() << endl; // Output: 3
    minStack.pop();
    cout << minStack.getMin() << endl; // Output: 3
    minStack.pop();
    cout << minStack.getMin() << endl; // Output: 5
    return 0;
}
```

## Test Cases
```
Input: push(5), push(3), push(7), getMin, pop, getMin
Output: 3, 5
Input: push(1), push(2), push(3), getMin, pop, getMin
Output: 1, 1
```

## Key Takeaways
- Use of two stacks to keep track of the minimum element at each step
- Updating the min stack whenever an element is pushed or popped from the main stack
- Ensuring the min stack remains non-empty to avoid exceptions when calling getMin()