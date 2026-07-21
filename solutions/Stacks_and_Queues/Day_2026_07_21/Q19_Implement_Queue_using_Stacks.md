# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element that is added will be the first one to be removed. The queue should support the following operations: `push(x)`, `pop()`, `peek()`, and `empty()`. The `push(x)` operation adds an element `x` to the end of the queue. The `pop()` operation removes the element from the front of the queue. The `peek()` operation returns the element at the front of the queue without removing it. The `empty()` operation checks if the queue is empty.

## Approach
We can implement a queue using two stacks by using one stack for enqueue operations and the other stack for dequeue operations. When an element is pushed into the queue, it is added to the top of the first stack. When an element is popped from the queue, the elements are transferred from the first stack to the second stack, and then the top element is removed from the second stack.

## Complexity
- Time: O(1) for push and empty operations, O(n) for pop and peek operations in the worst case (when the second stack is empty)
- Space: O(n) for storing the elements in the two stacks

## C++ Solution
```cpp
#include <stack>

class MyQueue {
private:
    std::stack<int> stackNewestOnTop; // stack to store new elements
    std::stack<int> stackOldestOnTop; // stack to store old elements

public:
    /** Push element x to the back of queue. */
    void push(int x) {
        stackNewestOnTop.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        shiftStacks();
        int front = stackOldestOnTop.top();
        stackOldestOnTop.pop();
        return front;
    }

    /** Get the front element. */
    int peek() {
        shiftStacks();
        return stackOldestOnTop.top();
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        return stackNewestOnTop.empty() && stackOldestOnTop.empty();
    }

    // helper function to transfer elements from stackNewestOnTop to stackOldestOnTop
    void shiftStacks() {
        if (stackOldestOnTop.empty()) {
            while (!stackNewestOnTop.empty()) {
                stackOldestOnTop.push(stackNewestOnTop.top());
                stackNewestOnTop.pop();
            }
        }
    }
};
```

## Test Cases
```
Input: MyQueue queue; queue.push(1); queue.push(2); queue.peek(); queue.pop(); queue.empty();
Output: 1, 1, true
```

## Key Takeaways
- We use two stacks to implement a queue, one for enqueue operations and the other for dequeue operations.
- The `shiftStacks` function is used to transfer elements from the new stack to the old stack when the old stack is empty.
- The time complexity of push and empty operations is O(1), while the time complexity of pop and peek operations is O(n) in the worst case.