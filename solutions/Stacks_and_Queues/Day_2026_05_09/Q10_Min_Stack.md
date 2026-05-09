# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and getMin operations, where getMin returns the minimum element in the stack. The stack should be able to handle duplicate elements and the getMin operation should return the correct minimum element even after multiple push and pop operations. The constraints are: -2^31 <= x <= 2^31 - 1, where x is the element being pushed onto the stack. The stack will not be empty when getMin is called.

## Approach
We can use two stacks to solve this problem, one for the actual elements and another to keep track of the minimum elements. The second stack will be updated whenever a new minimum element is pushed onto the first stack. We will use the second stack to get the minimum element in O(1) time.

## Complexity
- Time: O(1) for all operations (push, pop, top, getMin)
- Space: O(n), where n is the number of elements in the stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MinStack {
private:
    stack<int> st;
    stack<int> minSt;

public:
    void push(int x) {
        st.push(x);
        if (minSt.empty() || x <= minSt.top()) {
            minSt.push(x);
        }
    }

    void pop() {
        if (!st.empty()) {
            if (st.top() == minSt.top()) {
                minSt.pop();
            }
            st.pop();
        }
    }

    int top() {
        return st.top();
    }

    int getMin() {
        return minSt.top();
    }
};
```

## Test Cases
```
Input: MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
Output: minStack.getMin(); // return -3
minStack.pop();
Output: minStack.top(); // return 0
Output: minStack.getMin(); // return -2
```

## Key Takeaways
- Use two stacks to keep track of the actual elements and the minimum elements.
- Update the second stack whenever a new minimum element is pushed onto the first stack.
- Use the second stack to get the minimum element in O(1) time.