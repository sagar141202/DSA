# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should support the following operations: push(x) -- Push element x onto the stack, pop() -- Removes the element on top of the stack, top() -- Get the top element, and getMin() -- Retrieve the minimum element in the stack. The input will contain at most 1000 operations, and the input element will be between -10^4 and 10^4.

## Approach
We will use two stacks to solve this problem. The first stack will store the actual elements, and the second stack will store the minimum elements seen so far. When we push an element onto the first stack, we will also push the minimum of the current element and the top of the second stack onto the second stack. This way, the top of the second stack will always contain the minimum element in the first stack.

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
```

## Test Cases
```
Input: MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
Output: minStack.getMin() = -3
minStack.pop();
Output: minStack.top() = 0
Output: minStack.getMin() = -2
```

## Key Takeaways
- Use two stacks to keep track of the minimum element.
- Push the minimum of the current element and the top of the min stack onto the min stack when pushing an element onto the main stack.
- Pop the top element from the min stack when popping an element from the main stack if they are equal.