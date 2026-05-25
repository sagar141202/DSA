# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element that is added will be the first one to be removed. The queue should support the following operations: `push(x)` - Push element x to the back of queue, `pop()` - Removes the element from the front of queue, `peek()` - Get the front element, `empty()` - Return whether the queue is empty. The input will be a sequence of operations, and the output should be the result of each operation.

## Approach
We can implement a queue using two stacks by using one stack for storing new elements and the other stack for storing elements in the correct order. When an element is pushed, it is added to the first stack. When an element is popped or peeked, we check if the second stack is empty. If it is, we transfer all elements from the first stack to the second stack.

## Complexity
- Time: O(1) for push operation, O(n) for pop and peek operations in the worst case (when the second stack is empty)
- Space: O(n) for storing elements in the two stacks

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MyQueue {
private:
    stack<int> s1;
    stack<int> s2;

public:
    /** Push element x to the back of queue. */
    void push(int x) {
        // Add element to the first stack
        s1.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        // Check if the second stack is empty
        if (s2.empty()) {
            // Transfer all elements from the first stack to the second stack
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        // Remove and return the top element from the second stack
        int top = s2.top();
        s2.pop();
        return top;
    }

    /** Get the front element. */
    int peek() {
        // Check if the second stack is empty
        if (s2.empty()) {
            // Transfer all elements from the first stack to the second stack
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        // Return the top element from the second stack
        return s2.top();
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        // Check if both stacks are empty
        return s1.empty() && s2.empty();
    }
};
```

## Test Cases
```
Input: MyQueue q; q.push(1); q.push(2); q.push(3); q.pop(); q.peek();
Output: 1, 2
```

## Key Takeaways
- We can use two stacks to implement a queue by storing new elements in one stack and transferring them to the other stack when needed.
- The time complexity of push operation is O(1), while the time complexity of pop and peek operations is O(n) in the worst case.
- The space complexity is O(n) for storing elements in the two stacks.