# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should be able to handle duplicates and negative numbers. The constraints are: -2^31 <= x <= 2^31 - 1, where x is the value being pushed or popped. The problem requires implementing the following methods: `push(x)`, `pop()`, `top()`, and `getMin()`. For example, given the sequence of operations `push(-2)`, `push(0)`, `push(-3)`, `getMin()`, `pop()`, `top()`, `getMin()`, the output should be `-3`, `0`, `-2`.

## Approach
We will use two stacks to solve this problem: one for storing the actual elements and another for storing the minimum elements. The second stack will keep track of the minimum element at each step. When an element is pushed, we will check if it is smaller than or equal to the current minimum. If it is, we will push it onto the second stack. When an element is popped, we will check if it is equal to the current minimum. If it is, we will pop the top element from the second stack.

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
Input: MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
Output: minStack.getMin() = -3
minStack.pop();
Output: minStack.top() = 0
Output: minStack.getMin() = -2
```

## Key Takeaways
- Using two stacks allows us to keep track of the minimum element in constant time.
- We only push elements onto the second stack when they are smaller than or equal to the current minimum, which reduces the space complexity.
- Popping elements from the second stack when they are equal to the current minimum ensures that the second stack always contains the minimum element.