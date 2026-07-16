# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added to the queue will be the first one to be removed. The queue should support the following operations: `push(x)` - Push element x to the back of queue, `pop()` - Removes the element from the front of queue, `peek()` - Get the front element, and `empty()` - Return whether the queue is empty. The input will be a sequence of these operations, and the output should be the result of each operation. For example, given the sequence of operations `["MyQueue", "push", "1", "push", "2", "peek", "pop", "empty"]`, the output should be `[null, null, null, 1, 1, false]`.

## Approach
We can use two stacks to implement a queue. The first stack will be used to store the elements in the order they are added, and the second stack will be used to store the elements in the reverse order. When an element is added to the queue, it will be pushed onto the first stack. When an element is removed from the queue, it will be popped from the second stack if it is not empty, or the elements will be transferred from the first stack to the second stack and then popped.

## Complexity
- Time: O(1) for push, O(1) amortized for pop and peek, O(1) for empty
- Space: O(n), where n is the number of elements in the queue

## C++ Solution
```cpp
#include <stack>

class MyQueue {
private:
    std::stack<int> inStack;
    std::stack<int> outStack;

public:
    MyQueue() {}

    void push(int x) {
        // Push element x to the back of queue
        inStack.push(x);
    }

    int pop() {
        // Removes the element from the front of queue
        if (outStack.empty()) {
            while (!inStack.empty()) {
                outStack.push(inStack.top());
                inStack.pop();
            }
        }
        int top = outStack.top();
        outStack.pop();
        return top;
    }

    int peek() {
        // Get the front element
        if (outStack.empty()) {
            while (!inStack.empty()) {
                outStack.push(inStack.top());
                inStack.pop();
            }
        }
        return outStack.top();
    }

    bool empty() {
        // Return whether the queue is empty
        return inStack.empty() && outStack.empty();
    }
};
```

## Test Cases
```
Input: ["MyQueue", "push", "1", "push", "2", "peek", "pop", "empty"]
Output: [null, null, null, 1, 1, false]
```

## Key Takeaways
- We can use two stacks to implement a queue by transferring elements from one stack to another when necessary.
- The time complexity for push is O(1), and the time complexity for pop and peek is O(1) amortized.
- The space complexity is O(n), where n is the number of elements in the queue.