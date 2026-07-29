# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. The queue should support the following operations: `push(x)` - Push element x to the back of queue, `pop()` - Removes the element from the front of queue, and `peek()` - Get the front element, `empty()` - Return whether the queue is empty. The queue should follow the First-In-First-Out (FIFO) principle.

## Approach
We can use two stacks to implement a queue. The first stack will be used for pushing elements and the second stack will be used for popping and peeking elements. When an element is pushed, it will be added to the first stack. When an element is popped or peeked, we will transfer all elements from the first stack to the second stack, and then pop or peek the top element from the second stack.

## Complexity
- Time: O(1) for push, O(n) for pop and peek in the worst case
- Space: O(n)

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
        // Push the element to the first stack
        s1.push(x);
    }

    /** Removes the element from the front of queue and return it. */
    int pop() {
        // If the second stack is empty, transfer all elements from the first stack to the second stack
        if (s2.empty()) {
            while (!s1.empty()) {
                // Transfer the elements
                s2.push(s1.top());
                s1.pop();
            }
        }
        // Pop and return the top element from the second stack
        int top = s2.top();
        s2.pop();
        return top;
    }

    /** Get the front element. */
    int peek() {
        // If the second stack is empty, transfer all elements from the first stack to the second stack
        if (s2.empty()) {
            while (!s1.empty()) {
                // Transfer the elements
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
Input: ["MyQueue","push","push","peek","pop","empty"]
Output: [null,null,null,1,1,false]
Input: ["MyQueue","push","push","pop","pop","empty", "peek"]
Output: [null,null,null,1,2,true, error]
```

## Key Takeaways
- We use two stacks to implement a queue, one for pushing elements and one for popping and peeking elements.
- The `push` operation has a time complexity of O(1), while the `pop` and `peek` operations have a time complexity of O(n) in the worst case.
- The space complexity is O(n), where n is the number of elements in the queue.