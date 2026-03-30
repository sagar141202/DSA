# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should be able to handle duplicate elements and negative numbers. The minStack class should have the following methods: push(x) -- Push element x onto stack, pop() -- Removes the element on top of the stack, top() -- Get the top element, and getMin() -- Retrieve the minimum element in the stack. For example, given the sequence of operations ["MinStack","push","push","push","getMin","pop","top","getMin"], with inputs [[],[-2],[0],[-3],[],[],[],[]], the output should be [null,null,null,null,-3,null,0,-2].

## Approach
We will use two stacks to solve this problem, one for storing the actual elements and the other for storing the minimum elements. When we push an element, we check if the min stack is empty or the new element is less than or equal to the current minimum. If it is, we push the new element to the min stack as well.

## Complexity
- Time: O(1)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MinStack {
public:
    stack<int> mainStack;
    stack<int> minStack;

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
Inputs: [[],[-2],[0],[-3],[],[],[],[]]
Output: [null,null,null,null,-3,null,0,-2]
```

## Key Takeaways
- We use two stacks to keep track of the minimum element at all times.
- The minStack is updated only when a new minimum element is pushed to the mainStack.
- The time complexity is O(1) because we are performing constant time operations (push and pop) on the stacks.