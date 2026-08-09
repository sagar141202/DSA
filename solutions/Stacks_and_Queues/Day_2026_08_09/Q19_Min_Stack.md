# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should handle duplicates and negative numbers. For example, given the sequence of operations: push(-2), push(0), push(-3), getMin(), top(), pop(), getMin(), the output should be -3, 0, -2.

## Approach
We will use two stacks, one for storing the actual elements and another for storing the minimum elements. When an element is pushed, we will check if it's smaller than or equal to the current minimum and update the minimum stack accordingly.

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
System.out.println(minStack.getMin()); // Output: -3
System.out.println(minStack.top()); // Output: -3
minStack.pop();
System.out.println(minStack.top()); // Output: 0
System.out.println(minStack.getMin()); // Output: -2
```

## Key Takeaways
- Using two stacks allows for efficient retrieval of the minimum element in constant time.
- The minStack is updated only when a smaller or equal element is pushed, ensuring the top of minStack always holds the current minimum.