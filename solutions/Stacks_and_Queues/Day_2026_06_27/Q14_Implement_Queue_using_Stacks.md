# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element that is added will be the first one to be removed. The queue should support the following operations: `push(x)` - Push element x to the back of queue, `pop()` - Removes the element from the front of queue, `peek()` - Get the front element, `empty()` - Return whether the queue is empty. The input will be a series of operations, and the output should be the result of each operation. For example, given the operations `push(1)`, `push(2)`, `peek()`, `pop()`, `empty()`, the output should be `1`, `1`.

## Approach
We can use two stacks to implement a queue. The first stack will be used to store the new elements, and the second stack will be used to store the elements in the correct order. When an element is pushed, it is added to the first stack. When an element is popped or peeked, the elements are transferred from the first stack to the second stack if the second stack is empty.

## Complexity
- Time: O(1) for push, O(n) for pop and peek in the worst case
- Space: O(n)

## C++ Solution
```cpp
#include <stack>

class MyQueue {
private:
    std::stack<int> stackNewestOnTop; // stack to store new elements
    std::stack<int> stackOldestOnTop; // stack to store elements in the correct order

public:
    MyQueue() {}

    // Push element x to the back of queue
    void push(int x) {
        stackNewestOnTop.push(x);
    }

    // Removes the element from the front of queue
    int pop() {
        shiftStacks();
        int front = stackOldestOnTop.top();
        stackOldestOnTop.pop();
        return front;
    }

    // Get the front element
    int peek() {
        shiftStacks();
        return stackOldestOnTop.top();
    }

    // Return whether the queue is empty
    bool empty() {
        return stackNewestOnTop.empty() && stackOldestOnTop.empty();
    }

    // Shift elements from stackNewestOnTop to stackOldestOnTop if stackOldestOnTop is empty
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
Input: push(1), push(2), peek(), pop(), empty()
Output: 1, 1, false
```

## Key Takeaways
- We can use two stacks to implement a queue, where one stack stores new elements and the other stack stores elements in the correct order.
- The `push` operation has a time complexity of O(1), while the `pop` and `peek` operations have a time complexity of O(n) in the worst case.
- The space complexity is O(n), where n is the number of elements in the queue.