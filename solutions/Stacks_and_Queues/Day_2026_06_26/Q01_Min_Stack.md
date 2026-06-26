# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should support the following operations: push(x) - Push element x onto stack, pop() - Removes the element on top of the stack, top() - Get the top element, and getMin() - Retrieve the minimum element in the stack. The input will be a series of operations, and the output should be the result of each operation. The stack will not be empty when pop, top, or getMin is called.

## Approach
We can use two stacks to solve this problem, one for storing the actual elements and another for storing the minimum elements. The algorithm will ensure that the top of the min stack always has the minimum element.

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
Input: 
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output: 
[null,null,null,null,-3,null,0,-2]
```

## Key Takeaways
- Using two stacks to keep track of the minimum element at each step is an effective approach.
- The min stack should only be updated when a new minimum is pushed or when the top element of the main stack is equal to the top element of the min stack and is popped.