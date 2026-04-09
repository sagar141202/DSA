# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added to the queue will be the first one to be removed. The queue should support the following operations: `push(x)` - Push element x to the back of queue, `pop()` - Removes the element from the front of queue, `peek()` - Get the front element, `empty()` - Return whether the queue is empty. The input will be a sequence of these operations. For example, `push(1)`, `push(2)`, `peek()`, `pop()`, `empty()`.

## Approach
We will use two stacks, one for enqueue and one for dequeue. When an element is pushed, it will be added to the first stack. When an element is popped or peeked, we will transfer elements from the first stack to the second stack until the top element of the first stack is the one we want to pop or peek.

## Complexity
- Time: O(1) for push, O(n) for pop and peek in the worst case (when the second stack is empty), where n is the number of elements in the queue
- Space: O(n), where n is the total number of elements in the queue

## C++ Solution
```cpp
#include <stack>

class MyQueue {
private:
    std::stack<int> stackNewestOnTop; // stack for enqueue
    std::stack<int> stackOldestOnTop; // stack for dequeue

public:
    MyQueue() {}

    void push(int x) {
        // simply push the element to the first stack
        stackNewestOnTop.push(x);
    }

    int pop() {
        // if the second stack is empty, transfer elements from the first stack
        if (stackOldestOnTop.empty()) {
            while (!stackNewestOnTop.empty()) {
                stackOldestOnTop.push(stackNewestOnTop.top());
                stackNewestOnTop.pop();
            }
        }
        // pop the top element from the second stack
        int top = stackOldestOnTop.top();
        stackOldestOnTop.pop();
        return top;
    }

    int peek() {
        // if the second stack is empty, transfer elements from the first stack
        if (stackOldestOnTop.empty()) {
            while (!stackNewestOnTop.empty()) {
                stackOldestOnTop.push(stackNewestOnTop.top());
                stackNewestOnTop.pop();
            }
        }
        // return the top element from the second stack
        return stackOldestOnTop.top();
    }

    bool empty() {
        // the queue is empty if both stacks are empty
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
- We can use two stacks to implement a queue, with one stack for enqueue and one stack for dequeue.
- The `pop` and `peek` operations may require transferring elements from the first stack to the second stack, resulting in a worst-case time complexity of O(n).
- The space complexity is O(n), where n is the total number of elements in the queue.