# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should handle duplicates and negative numbers. For example, given the sequence of operations `push(1)`, `push(2)`, `push(0)`, `min()`, `pop()`, `top()`, `min()`, the output should be `0`, `1`, `0` respectively. The stack should be able to handle a maximum of 10000 operations.

## Approach
We will use two stacks to solve this problem: one for storing the actual elements and another for keeping track of the minimum elements. When an element is pushed, we check if the min stack is empty or the element is less than or equal to the top of the min stack. If it is, we push the element to the min stack.

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
    void push(int val) {
        mainStack.push(val);
        if (minStack.empty() || val <= minStack.top()) {
            minStack.push(val);
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
        return -1; // or throw an exception
    }

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
Input: push(1), push(2), push(0), min(), pop(), top(), min()
Output: 0, 1, 0
```

## Key Takeaways
- Use two stacks to keep track of the actual elements and the minimum elements.
- When pushing an element, check if it's less than or equal to the top of the min stack and push it to the min stack if necessary.
- When popping an element, check if it's equal to the top of the min stack and pop it from the min stack if necessary.