# Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. The stack should be able to handle duplicate elements and negative numbers. For example, given the sequence of operations: ["MinStack","push","push","push","getMin","pop","getMin"], with inputs: [[],[-2],[0],[-3],[],[0],[-3]], the output should be: [null,null,null,null,-3,null,-2]. The constraints are: 1 <= x <= 10^5, at most 10^4 calls will be made to push, pop, top, and getMin.

## Approach
We can use two stacks to solve this problem, one for storing the actual elements and another for storing the minimum elements. When an element is pushed, we check if the min stack is empty or the new element is smaller than or equal to the top of the min stack. If it is, we push the new element to the min stack. When an element is popped, we check if it is equal to the top of the min stack. If it is, we pop the top element from the min stack.

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
Inputs: [[],[-2],[0],[-3],[],[0],[-3]]
Output: [null,null,null,null,-3,null,-2]
```

## Key Takeaways
- We use two stacks to keep track of the actual elements and the minimum elements.
- The min stack is updated only when a smaller or equal element is pushed.
- When an element is popped, we check if it is equal to the top of the min stack and update the min stack accordingly.