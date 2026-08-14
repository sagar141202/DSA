# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element that is added will be the first one to be removed. The queue should support the following operations: `push(x)`, `pop()`, `peek()`, `empty()`. The `push(x)` operation adds an element `x` to the end of the queue. The `pop()` operation removes the element from the front of the queue. The `peek()` operation returns the element from the front of the queue without removing it. The `empty()` operation checks if the queue is empty.

## Approach
We can use two stacks to implement a queue. The first stack will be used to store the elements in the order they are added, and the second stack will be used to store the elements in the reverse order. When an element is added to the queue, it is pushed onto the first stack. When an element is removed from the queue, the elements are popped from the first stack and pushed onto the second stack, and then the top element is popped from the second stack.

## Complexity
- Time: O(1) for `push(x)` and `empty()`, O(n) for `pop()` and `peek()` in the worst case
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MyQueue {
private:
    stack<int> s1, s2;
public:
    /** Push element x to the back of queue. */
    void push(int x) {
        s1.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        int x = s2.top();
        s2.pop();
        return x;
    }

    /** Get the front element. */
    int peek() {
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        return s2.top();
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        return s1.empty() && s2.empty();
    }
};
```

## Test Cases
```
Input: ["MyQueue", "push", "push", "peek", "pop", "empty"]
Output: [null, null, null, 1, 1, false]
```

## Key Takeaways
- Use two stacks to implement a queue, one for storing elements in the order they are added and another for storing elements in the reverse order.
- When an element is added to the queue, push it onto the first stack.
- When an element is removed from the queue, pop elements from the first stack and push them onto the second stack, and then pop the top element from the second stack.