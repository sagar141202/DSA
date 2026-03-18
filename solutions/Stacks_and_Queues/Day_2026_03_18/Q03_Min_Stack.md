# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the `MinStack` class: 
- `MinStack()` initializes the stack.
- `void push(int x)` pushes element `x` onto the stack.
- `void pop()` removes the element on top of the stack.
- `int top()` gets the top element.
- `int getMin()` retrieves the minimum element in the stack.
The stack will not be empty when `pop`, `top`, or `getMin` is called. The input will not exceed 1000 operations, and all elements are within the range [-10^4, 10^4].

## Approach
We will use two stacks to solve this problem: one for storing the actual elements and another for keeping track of the minimum elements. The second stack will be updated whenever a new minimum element is pushed onto the first stack. This way, we can retrieve the minimum element in constant time.

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
    MinStack() {}

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
Output: minStack.getMin() // return -3
minStack.pop();
Output: minStack.top() // return 0
Output: minStack.getMin() // return -2
```

## Key Takeaways
- Use of two stacks to keep track of the minimum element in constant time.
- Update the second stack only when a new minimum element is pushed onto the first stack.
- Remove the top element from the second stack when the top element of the first stack is popped and it is the current minimum.