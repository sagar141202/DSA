# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added will be the first one to be removed. The queue should support the following operations: `push(x)` - Push element x to the back of the queue, `pop()` - Removes the element from the front of the queue, `peek()` - Get the front element, and `empty()` - Return whether the queue is empty. The queue should handle a maximum of 1000 operations and the input values will be in the range of 1 to 1000.

## Approach
We can implement a queue using two stacks by using one stack for enqueue operations and the other stack for dequeue operations. When an element is pushed into the queue, it is added to the top of the first stack. When an element is popped from the queue, we transfer elements from the first stack to the second stack, and then pop the top element from the second stack.

## Complexity
- Time: O(1) for push and empty operations, O(n) for pop and peek operations in the worst case
- Space: O(n) where n is the number of elements in the queue

## C++ Solution
```cpp
#include <stack>

class MyQueue {
private:
    std::stack<int> stackNewestOnTop; // newest element on top
    std::stack<int> stackOldestOnTop; // oldest element on top

public:
    MyQueue() {}

    void push(int x) {
        // push onto the newest stack
        stackNewestOnTop.push(x);
    }

    void pop() {
        // if the oldest stack is empty, transfer elements from the newest stack
        if (stackOldestOnTop.empty()) {
            while (!stackNewestOnTop.empty()) {
                stackOldestOnTop.push(stackNewestOnTop.top());
                stackNewestOnTop.pop();
            }
        }
        // pop from the oldest stack
        stackOldestOnTop.pop();
    }

    int peek() {
        // if the oldest stack is empty, transfer elements from the newest stack
        if (stackOldestOnTop.empty()) {
            while (!stackNewestOnTop.empty()) {
                stackOldestOnTop.push(stackNewestOnTop.top());
                stackNewestOnTop.pop();
            }
        }
        // return the top of the oldest stack
        return stackOldestOnTop.top();
    }

    bool empty() {
        // check if both stacks are empty
        return stackNewestOnTop.empty() && stackOldestOnTop.empty();
    }
};
```

## Test Cases
```
Input: push(1), push(2), peek(), pop(), empty()
Output: 1, 1, false
```

## Key Takeaways
- Using two stacks allows us to efficiently implement a queue with O(1) time complexity for push and empty operations.
- The pop and peek operations have a worst-case time complexity of O(n), but this occurs only when the oldest stack is empty and we need to transfer elements from the newest stack.