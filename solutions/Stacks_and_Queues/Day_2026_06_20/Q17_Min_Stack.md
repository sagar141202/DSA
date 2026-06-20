# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the MinStack class: 
- MinStack() initializes the stack.
- void push(int x) pushes element x onto the stack.
- void pop() removes the element on top of the stack.
- int top() gets the top element.
- int getMin() retrieves the minimum element in the stack. 
You can assume that all operations are valid (i.e., pop, top, and getMin will not be called on an empty stack).

## Approach
We can use two stacks to solve this problem, one for storing the actual elements and another for keeping track of the minimum elements. The algorithm pushes elements onto the main stack and updates the min stack whenever a smaller element is encountered.

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
Input: push(-2), push(0), push(-3), getMin(), pop(), top(), getMin()
```

## Key Takeaways
- We used two stacks, mainStack and minStack, to keep track of the actual elements and the minimum elements, respectively.
- When pushing an element, we check if it's smaller than or equal to the current minimum and update minStack accordingly.
- When popping an element, we check if it's equal to the current minimum and update minStack if necessary.