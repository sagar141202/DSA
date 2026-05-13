# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should support the following operations: push(x) -- Push element x onto stack, pop() -- Removes the element on top of the stack, top() -- Get the top element, and getMin() -- Retrieve the minimum element in the stack. The stack will contain only positive integers, and all the operations should be performed in constant time.

## Approach
To solve this problem, we can use two stacks: one for storing the actual elements and another for storing the minimum elements. We update the minimum stack whenever we push or pop an element from the main stack. This way, we can retrieve the minimum element in constant time.

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
- We use two stacks to keep track of the actual elements and the minimum elements.
- The time complexity for all operations (push, pop, top, getMin) is O(1) because we are using stacks.
- The space complexity is O(n) because in the worst case, we might need to store all elements in both stacks.