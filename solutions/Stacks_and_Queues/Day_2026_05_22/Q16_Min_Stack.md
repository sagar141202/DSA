# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack will be populated with non-negative integers. The min stack should support the following operations: push(x) -- Push element x onto stack, pop() -- Removes the element on top of the stack, top() -- Get the top element, getMin() -- Retrieve the minimum element in the stack. For example, given the sequence of operations: ["MinStack","push","push","push","getMin","pop","top","getMin"], [[],[-2],[0],[-3],[],[],[],[]], the output should be: [null,null,null,null,-3,null,0,-2].

## Approach
We will use two stacks to implement the min stack: one for storing the actual elements and another for keeping track of the minimum elements. The min stack will be updated whenever an element is pushed or popped from the main stack. This allows us to retrieve the minimum element in constant time.

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
Input: 
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output: 
[null,null,null,null,-3,null,0,-2]
```

## Key Takeaways
- Using two stacks allows for efficient retrieval of the minimum element in constant time.
- The min stack should only store the minimum elements seen so far to avoid unnecessary space usage.
- The main stack and min stack should be updated simultaneously to maintain consistency.