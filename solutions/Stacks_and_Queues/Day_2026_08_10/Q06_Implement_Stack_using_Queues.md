# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The given queues are standard queues with enqueue and dequeue operations. The constraints are that we can only use these two queues to implement the stack, and we should minimize the number of queue operations. For example, if we push the elements 1, 2, and 3 into the stack, the top of the stack should be 3, and after popping an element, the top of the stack should be 2.

## Approach
We will use two queues, q1 and q2, to implement the stack. For the push operation, we will always enqueue the new element into q1. For the pop operation, we will dequeue all elements from q1 and enqueue them into q2, except for the last element, which we will return as the popped element. Then, we will swap the roles of q1 and q2.

## Complexity
- Time: O(n) for pop operation, O(1) for push operation
- Space: O(n), where n is the number of elements in the stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Stack {
private:
    queue<int> q1;
    queue<int> q2;

public:
    // Push element x onto stack
    void push(int x) {
        q1.push(x);
    }

    // Removes the element on top of the stack
    void pop() {
        if (q1.empty()) {
            return;
        }
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        q1.pop();
        swap(q1, q2);
    }

    // Get the top element
    int top() {
        if (q1.empty()) {
            return -1;
        }
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        int topElement = q1.front();
        q2.push(q1.front());
        q1.pop();
        swap(q1, q2);
        return topElement;
    }

    // Return whether the stack is empty
    bool empty() {
        return q1.empty();
    }
};
```

## Test Cases
```
Input: push(1), push(2), push(3), pop(), top()
Output: 2
```

## Key Takeaways
- We can implement a stack using two queues by using one queue for storing the elements and the other queue for temporary storage during the pop operation.
- The time complexity of the push operation is O(1), while the time complexity of the pop operation is O(n), where n is the number of elements in the stack.
- The space complexity is O(n), where n is the number of elements in the stack.