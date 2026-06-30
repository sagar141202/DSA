# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should support the following operations: push(x) -- Push element x onto stack, pop() -- Removes the element on top of the stack, top() -- Get the top element, and getMin() -- Retrieve the minimum element in the stack. The input will be a series of operations, and the output should be the result of each operation. For example, if we have the operations ["MinStack","push(-2)","push(0)","push(-3)","getMin","pop","top","getMin"], the output should be [null,null,null,null,-3,null,0,-2].

## Approach
We can use two stacks, one for storing the actual elements and another for storing the minimum elements at each step. When we push an element, we also push the current minimum into the min stack if the new element is smaller or equal to the current minimum. When we pop an element, we also pop from the min stack if the popped element is equal to the current minimum.

## Complexity
- Time: O(1)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MinStack {
public:
    stack<int> s;
    stack<int> min_s;

    void push(int x) {
        s.push(x);
        if (min_s.empty() || x <= min_s.top()) {
            min_s.push(x);
        }
    }

    void pop() {
        if (!s.empty()) {
            if (s.top() == min_s.top()) {
                min_s.pop();
            }
            s.pop();
        }
    }

    int top() {
        if (!s.empty()) {
            return s.top();
        }
        return -1; // or throw an exception
    }

    int getMin() {
        if (!min_s.empty()) {
            return min_s.top();
        }
        return -1; // or throw an exception
    }
};
```

## Test Cases
```
Input: ["MinStack","push(-2)","push(0)","push(-3)","getMin","pop","top","getMin"]
Output: [null,null,null,null,-3,null,0,-2]
```

## Key Takeaways
- Use two stacks to keep track of the minimum element at each step.
- When pushing an element, also push the current minimum into the min stack if the new element is smaller or equal to the current minimum.
- When popping an element, also pop from the min stack if the popped element is equal to the current minimum.