# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and getMin operations, where getMin returns the minimum element in the stack. The stack should be able to handle duplicate elements and support standard stack operations. For example, given the operations `["MinStack","push","push","push","getMin","pop","getMin"]` with arguments `[[],[-2],[0],[-3],[],[],[]]`, the output should be `[null,null,null,null,-3,null,-2]`. The constraints are that the stack will not be empty when pop is called, and there will be at least one element in the stack when getMin is called.

## Approach
The algorithm uses two stacks, one for storing the actual elements and another for keeping track of the minimum elements. When an element is pushed onto the stack, it is also pushed onto the min stack if it is less than or equal to the current minimum. When an element is popped from the stack, it is also popped from the min stack if it is equal to the current minimum. This way, the min stack always contains the minimum element at its top.

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
        if (s.top() == min_s.top()) {
            min_s.pop();
        }
        s.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return min_s.top();
    }
};
```

## Test Cases
```
Input: ["MinStack","push","push","push","getMin","pop","getMin"]
Arguments: [[],[-2],[0],[-3],[],[],[]]
Output: [null,null,null,null,-3,null,-2]
```

## Key Takeaways
- Use two stacks to keep track of the actual elements and the minimum elements.
- When pushing an element, also push it onto the min stack if it is less than or equal to the current minimum.
- When popping an element, also pop it from the min stack if it is equal to the current minimum.