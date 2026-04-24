# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added will be the first one to be removed. The queue should support the following operations: `push(x)` - add element x to the end of the queue, `pop()` - remove the element from the front of the queue, `peek()` - get the element from the front of the queue without removing it, and `empty()` - check if the queue is empty. The input will be a series of these operations, and the output should be the result of each operation.

## Approach
We can implement a queue using two stacks by using one stack for enqueue operations and the other for dequeue operations. When an element is added to the queue, it is pushed onto the first stack. When an element is removed from the queue, we pop all elements from the first stack and push them onto the second stack, then pop the top element from the second stack.

## Complexity
- Time: O(1) for push and empty operations, O(n) for pop and peek operations in the worst case
- Space: O(n), where n is the number of elements in the queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MyQueue {
private:
    stack<int> s1, s2;
public:
    // Push element x to the back of queue.
    void push(int x) {
        s1.push(x);
    }

    // Removes the element from in front of queue.
    int pop() {
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        int top = s2.top();
        s2.pop();
        return top;
    }

    // Get the front element.
    int peek() {
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        return s2.top();
    }

    // Return whether the queue is empty.
    bool empty() {
        return s1.empty() && s2.empty();
    }
};
```

## Test Cases
```
Input: ["MyQueue", "push", "push", "peek", "pop", "empty"]
Output: [null, null, null, 1, 1, false]
Input: ["MyQueue", "push", "pop", "empty"]
Output: [null, null, null, true]
```

## Key Takeaways
- We use two stacks to implement a queue, which allows us to achieve FIFO order.
- The `push` operation has a time complexity of O(1) because we simply push the element onto the first stack.
- The `pop` and `peek` operations have a time complexity of O(n) in the worst case because we need to transfer all elements from the first stack to the second stack.