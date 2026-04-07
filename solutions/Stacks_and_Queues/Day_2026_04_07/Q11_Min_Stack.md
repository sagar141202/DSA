# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the `MinStack` class: 
- `MinStack()` initializes the stack.
- `void push(int x)` pushes element `x` onto the stack.
- `void pop()` removes the element on top of the stack.
- `int top()` gets the top element.
- `int getMin()` retrieves the minimum element in the stack.
Example: 
- `MinStack minStack = new MinStack();`
- `minStack.push(-2);`
- `minStack.push(0);`
- `minStack.push(-3);`
- `minStack.getMin();`  // return -3
- `minStack.pop();`
- `minStack.top();`     // return 0
- `minStack.getMin();`  // return -2

## Approach
The algorithm uses two stacks to keep track of the elements and the minimum values. One stack is used for storing the actual elements, and the other stack is used to keep track of the minimum elements at each step. This approach ensures that the `getMin` operation can be performed in constant time.

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
    MinStack() {}

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
        return -1; // or throw exception
    }

    int getMin() {
        if (!minStack.empty()) {
            return minStack.top();
        }
        return -1; // or throw exception
    }
};
```

## Test Cases
```
Input: 
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();  
minStack.pop();
minStack.top();     
minStack.getMin();  

Output: 
-3
0
-2
```

## Key Takeaways
- Using two stacks, one for the main elements and one for the minimum elements, allows for efficient `getMin` operation.
- The `push` operation checks if the new element is smaller than or equal to the current minimum, and if so, pushes it to the `minStack`.
- The `pop` operation checks if the top element of the `mainStack` is equal to the top element of the `minStack`, and if so, pops it from the `minStack` as well.