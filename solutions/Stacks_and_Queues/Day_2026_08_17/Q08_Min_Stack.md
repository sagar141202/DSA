# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack will be initialized with an empty stack, and the following methods will be called: 
- `void push(int x)`: Pushes element x onto stack.
- `void pop()`: Removes the element on top of the stack.
- `int top()`: Gets the top element.
- `int getMin()`: Retrieves the minimum element in the stack. 
The input will be a sequence of these operations, and the output will be the result of each operation. For example, if we have the sequence `["MinStack","push","push","push","getMin","pop","top","getMin"]` with the input values `["],[-2],[0],[-3],[],[],[],[]` the output will be `[null,null,null,null,-3,null,0,-2]`.

## Approach
We can use two stacks to solve this problem: one for storing the actual elements and another for storing the minimum elements seen so far. The second stack will be updated whenever we push or pop an element from the first stack.

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
Input: 
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output: 
[null,null,null,null,-3,null,0,-2]
```

## Key Takeaways
- Use of two stacks to keep track of the minimum element.
- The minStack is updated only when a smaller or equal element is pushed onto the mainStack.
- When the top element of the mainStack is the same as the top element of the minStack, we pop from both stacks during the pop operation.