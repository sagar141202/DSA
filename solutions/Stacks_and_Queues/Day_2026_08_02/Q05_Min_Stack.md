# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should support the following operations: push(x) -- Push element x onto stack, pop() -- Removes the element on top of the stack, top() -- Get the top element, and getMin() -- Retrieve the minimum element in the stack. The stack will be empty initially, and all operations will be valid. You may assume that all operations are valid and follow the format: ["MinStack","push","push","push","getMin","pop","top","getMin"] and [["],[-2],[0],[-3],[],[],[],[]].

## Approach
We will use two stacks, one for storing the actual elements and another for storing the minimum elements. When an element is pushed, we check if the min stack is empty or the current element is less than or equal to the top of the min stack. If it is, we push the current element to the min stack. When an element is popped, we check if it is equal to the top of the min stack. If it is, we pop the top element from the min stack.

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
Input: ["MinStack","push","push","push","getMin","pop","top","getMin"]
Input Values: [[],[-2],[0],[-3],[],[],[],[]]
Output: [null,null,null,null,-3,null,0,-2]
```

## Key Takeaways
- Use of two stacks to keep track of the minimum element in constant time
- The min stack is updated only when a smaller element is pushed or when the top element of the main stack is popped and it is equal to the top of the min stack.