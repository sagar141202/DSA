# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added to the queue will be the first one to be removed. The queue should support the following operations: `push(x)`, `pop()`, `peek()`, and `empty()`. The `push(x)` operation adds an element `x` to the end of the queue. The `pop()` operation removes the element from the front of the queue. The `peek()` operation returns the element at the front of the queue without removing it. The `empty()` operation checks if the queue is empty.

## Approach
We can use two stacks to implement a queue. One stack will be used to store the incoming elements, and the other stack will be used to store the elements in the correct order. When an element is added to the queue, it will be pushed onto the first stack. When an element is removed from the queue, it will be popped from the second stack. If the second stack is empty, we will pop all elements from the first stack and push them onto the second stack.

## Complexity
- Time: O(1) for push, O(1) for pop and peek when the second stack is not empty, and O(n) when the second stack is empty
- Space: O(n)

## C++ Solution
```cpp
#include <stack>

class MyQueue {
private:
    std::stack<int> stackNewestOnTop; // stack to store new elements
    std::stack<int> stackOldestOnTop; // stack to store elements in the correct order

public:
    /** Push element x to the back of queue. */
    void push(int x) {
        // simply push the element onto the first stack
        stackNewestOnTop.push(x);
    }

    /** Removes the element from in front of queue and return that element. */
    int pop() {
        // if the second stack is empty, move all elements from the first stack to the second stack
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

    /** Get the front element. */
    int peek() {
        // if the second stack is empty, move all elements from the first stack to the second stack
        if (stackOldestOnTop.empty()) {
            while (!stackNewestOnTop.empty()) {
                stackOldestOnTop.push(stackNewestOnTop.top());
                stackNewestOnTop.pop();
            }
        }
        // return the top element from the second stack
        return stackOldestOnTop.top();
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        // the queue is empty if both stacks are empty
        return stackNewestOnTop.empty() && stackOldestOnTop.empty();
    }
};
```

## Test Cases
```
Input: MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek(); // returns 1
queue.pop(); // returns 1
queue.empty(); // returns false
```

## Key Takeaways
- We can use two stacks to implement a queue, where one stack stores the incoming elements and the other stack stores the elements in the correct order.
- The time complexity for push is O(1), and for pop and peek, it is O(1) when the second stack is not empty and O(n) when the second stack is empty.
- The space complexity is O(n), where n is the number of elements in the queue.