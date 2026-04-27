# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should be able to handle duplicates and negative numbers. For example, given the sequence of operations: ["MinStack","push","push","push","getMin","pop","getMin"], and the input values: [[],[-2],[0],[-3],[],[0],[]], the output should be: [null,null,null,null,-3,null,-2]. The constraints are: 1 <= x <= 10^5 for push operations, and -10^5 <= x <= 10^5 for getMin, pop, and top operations.

## Approach
We will use two stacks to solve this problem: one for storing the actual elements and another for keeping track of the minimum elements. When a new element is pushed, we check if the min stack is empty or the new element is smaller than or equal to the current minimum, and if so, we push it to the min stack. When an element is popped, we check if it's equal to the current minimum and if so, we pop the min stack as well.

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
Input: MinStack minStack = new MinStack();
       minStack.push(-2);
       minStack.push(0);
       minStack.push(-3);
       System.out.println(minStack.getMin()); // Output: -3
       minStack.pop();
       System.out.println(minStack.top()); // Output: 0
       System.out.println(minStack.getMin()); // Output: -2
```

## Key Takeaways
- Use two stacks to keep track of the actual elements and the minimum elements.
- Push elements to the min stack only when the new element is smaller than or equal to the current minimum.
- Pop elements from the min stack when the popped element is equal to the current minimum.