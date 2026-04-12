# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should support the following operations: push(x) -- Push element x onto stack, pop() -- Removes the element on top of the stack, top() -- Get the top element, and getMin() -- Retrieve the minimum element in the stack. The stack will not be empty when pop or top is called, and all the operations are guaranteed to be valid.

## Approach
We can use two stacks to solve this problem: one for storing the actual elements and another for storing the minimum elements. When we push an element, we also push the minimum of the current top and the new element onto the min stack. When we pop an element, we also pop the corresponding minimum element from the min stack.

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
        if (mainStack.top() == minStack.top()) {
            minStack.pop();
        }
        mainStack.pop();
    }

    int top() {
        return mainStack.top();
    }

    int getMin() {
        return minStack.top();
    }
};
```

## Test Cases
```
Input: MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
Output: minStack.getMin() == -3
minStack.pop();
Output: minStack.top() == 0
Output: minStack.getMin() == -2
```

## Key Takeaways
- Use two stacks to store actual elements and minimum elements.
- When pushing an element, also push the minimum of the current top and the new element onto the min stack.
- When popping an element, also pop the corresponding minimum element from the min stack if necessary.