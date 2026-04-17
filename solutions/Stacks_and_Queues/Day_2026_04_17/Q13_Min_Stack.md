# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the `MinStack` class: 
- `MinStack()` initializes the stack.
- `void push(int x)` pushes element `x` onto the stack.
- `void pop()` removes the element on top of the stack.
- `int top()` gets the top element.
- `int getMin()` retrieves the minimum element in the stack.
The stack will not be empty when `pop`, `top`, or `getMin` is called.

## Approach
We use two stacks: one for storing the actual elements and another for keeping track of the minimum elements. The second stack is updated whenever a new element is pushed or popped from the main stack. This allows us to retrieve the minimum element in constant time.

## Complexity
- Time: O(1)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MinStack {
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
Input: ["MinStack","push","push","push","getMin","pop","top","getMin"]
Output: [null,null,null,null,-3,null,0,-2]
```

## Key Takeaways
- Use an auxiliary stack to keep track of the minimum elements.
- Update the auxiliary stack whenever the main stack is modified.
- This approach allows for constant time complexity for `getMin` operation.