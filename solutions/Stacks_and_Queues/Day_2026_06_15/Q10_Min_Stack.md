# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the `MinStack` class: 
- `MinStack()` initializes the stack.
- `void push(int x)` pushes element `x` onto the stack.
- `void pop()` removes the element on top of the stack.
- `int top()` gets the top element.
- `int getMin()` retrieves the minimum element in the stack.
Constraints: 
- `-2^31 <= x <= 2^31 - 1`
- Methods `pop`, `top`, and `getMin` operate when the stack is non-empty.
- At most `3 * 10^4` calls will be made to the methods.

## Approach
We use two stacks: one to store the actual elements and another to keep track of the minimum elements. The second stack is updated whenever a new minimum is found. The `getMin` operation can be performed in constant time by returning the top element of the second stack.

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
Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();     // return 0
minStack.getMin(); // return -2
```

## Key Takeaways
- Using two stacks allows for efficient `push`, `pop`, and `getMin` operations.
- The second stack only stores the minimum elements seen so far, reducing space complexity.
- The `getMin` operation can be performed in constant time by returning the top element of the second stack.