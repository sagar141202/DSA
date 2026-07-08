# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should support the following operations: push(x) -- Push element x onto stack, pop() -- Removes the element on top of the stack, top() -- Get the top element, and getMin() -- Retrieve the minimum element in the stack. The stack will not be empty when pop, top, or getMin is called, and all the operations are guaranteed to be valid.

## Approach
We can use two stacks to solve this problem: one for storing the actual elements and another for storing the minimum elements. When an element is pushed, we check if the min stack is empty or the top of the min stack is greater than or equal to the new element. If so, we push the new element onto the min stack.

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
Output: minStack.getMin(); // return -3
minStack.pop();
Output: minStack.top(); // return 0
Output: minStack.getMin(); // return -2
```

## Key Takeaways
- Using two stacks allows for constant time operations.
- The min stack only stores the minimum elements seen so far.
- The main stack stores all the elements in the order they were pushed.