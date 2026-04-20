# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should support the following operations: push(x) -- Push element x onto stack, pop() -- Removes the element on top of the stack, top() -- Get the top element, and getMin() -- Retrieve the minimum element in the stack. The stack will not be empty when pop, top, or getMin are called, and all the operations are guaranteed to be performed.

## Approach
We will use two stacks to solve this problem: one for storing the actual elements and another for keeping track of the minimum elements. When an element is pushed, we will check if the min stack is empty or the current element is smaller than or equal to the top of the min stack. If so, we will push the current element onto the min stack.

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
- We can use two stacks to keep track of the actual elements and the minimum elements.
- When an element is pushed, we need to check if the min stack is empty or the current element is smaller than or equal to the top of the min stack.
- When an element is popped, we need to check if the top of the main stack is equal to the top of the min stack, and if so, we need to pop the min stack as well.