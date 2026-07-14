# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should support the following operations: 
- `push(x)`: Push element x onto stack.
- `pop()`: Removes the element on top of the stack.
- `top()`: Get the top element.
- `getMin()`: Retrieve the minimum element in the stack.
The stack will be tested with a variety of inputs, including duplicate elements, negative numbers, and sequences of push and pop operations. For example, given the sequence of operations `push(-2)`, `push(0)`, `push(-3)`, `getMin()`, `pop()`, `top()`, `getMin()`, the output should be `-3`, `0`, `-2`.

## Approach
We will use two stacks to solve this problem, one for the main stack and another for keeping track of the minimum elements. The main stack will store all the elements, and the min stack will store the minimum elements seen so far. This approach allows us to maintain the minimum element in constant time.

## Complexity
- Time: O(1)
- Space: O(n)

## C++ Solution
```cpp
#include <stack>
using namespace std;

class MinStack {
private:
    stack<int> mainStack;
    stack<int> minStack;

public:
    // Push element x onto stack
    void push(int x) {
        mainStack.push(x);
        if (minStack.empty() || x <= minStack.top()) {
            minStack.push(x);
        }
    }

    // Removes the element on top of the stack
    void pop() {
        if (!mainStack.empty()) {
            if (mainStack.top() == minStack.top()) {
                minStack.pop();
            }
            mainStack.pop();
        }
    }

    // Get the top element
    int top() {
        if (!mainStack.empty()) {
            return mainStack.top();
        }
        return -1; // or throw an exception
    }

    // Retrieve the minimum element in the stack
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
Input: 
push(-2)
push(0)
push(-3)
getMin()
pop()
top()
getMin()
Output: 
-3
0
-2
```

## Key Takeaways
- Using two stacks, one for the main stack and another for keeping track of the minimum elements, allows us to maintain the minimum element in constant time.
- The min stack should only be updated when a new minimum element is pushed onto the main stack or when the top element of the main stack is popped and it is also the top element of the min stack.