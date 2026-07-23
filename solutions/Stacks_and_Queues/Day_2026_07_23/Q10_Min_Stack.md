# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should be able to store integers, and the min function should return the smallest element currently in the stack. The push function should add an element to the top of the stack, the pop function should remove the top element from the stack, and the top function should return the top element without removing it. The min function should return the minimum element in the stack. For example, if we have a stack with elements [5, 3, 8, 4, 2], the min function should return 2.

## Approach
We will use two stacks to solve this problem: one for storing the actual elements and another for storing the minimum elements. The second stack will always keep track of the minimum element at its top. When a new element is pushed, we will check if it's smaller than or equal to the current minimum. If it is, we will push it onto the second stack as well.

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
- We use two stacks to keep track of the actual elements and the minimum elements.
- The time complexity is O(1) because all operations (push, pop, top, min) take constant time.
- The space complexity is O(n) because in the worst-case scenario, we might need to store all elements in both stacks.