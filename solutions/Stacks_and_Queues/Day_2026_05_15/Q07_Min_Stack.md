# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should be able to handle duplicates and negative numbers. For example, given the sequence of operations `["MinStack","push(-2)","push(0)","push(-3)","getMin","pop","top","getMin"]`, the output should be `[null,null,null,null,-3,null,0,-2]`. The stack should be able to handle at least 10000 operations.

## Approach
We will use two stacks, one for storing the actual elements and another for storing the minimum elements at each step. This will allow us to retrieve the minimum element in constant time. We will update the minimum stack whenever we push or pop an element from the main stack.

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
Input: ["MinStack","push(-2)","push(0)","push(-3)","getMin","pop","top","getMin"]
Output: [null,null,null,null,-3,null,0,-2]
```

## Key Takeaways
- Using two stacks allows us to retrieve the minimum element in constant time.
- The minimum stack is updated whenever we push or pop an element from the main stack.
- This solution handles duplicates and negative numbers correctly.