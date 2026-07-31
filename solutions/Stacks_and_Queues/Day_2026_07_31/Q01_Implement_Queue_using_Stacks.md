# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element that is added will be the first one to be removed. The queue should support the following operations: `push(x)` - Push element x to the back of queue, `pop()` - Removes the element from the front of queue, `peek()` - Get the front element, `empty()` - Return whether the queue is empty. The input will be a series of operations, and the output should be the result of each operation. For example, given the operations `push(1)`, `push(2)`, `peek()`, `pop()`, `empty()`, the output should be `1`, `1`.

## Approach
We can use two stacks to implement a queue. The first stack will be used to store the incoming elements, and the second stack will be used to store the elements in the correct order. When an element is pushed, it is added to the first stack. When an element is popped or peeked, the elements are transferred from the first stack to the second stack if the second stack is empty.

## Complexity
- Time: O(1) for push, O(n) for pop and peek in the worst case
- Space: O(n)

## C++ Solution
```cpp
#include <stack>

class MyQueue {
private:
    std::stack<int> stack1;
    std::stack<int> stack2;

public:
    /** Push element x to the back of queue. */
    void push(int x) {
        stack1.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if (empty()) {
            return -1; // or throw an exception
        }
        if (stack2.empty()) {
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        int top = stack2.top();
        stack2.pop();
        return top;
    }

    /** Get the front element. */
    int peek() {
        if (empty()) {
            return -1; // or throw an exception
        }
        if (stack2.empty()) {
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        return stack2.top();
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        return stack1.empty() && stack2.empty();
    }
};
```

## Test Cases
```
Input: push(1), push(2), peek(), pop(), empty()
Output: 1, 1, false
```

## Key Takeaways
- A queue can be implemented using two stacks by transferring elements from one stack to another when necessary.
- The time complexity for push is O(1), but for pop and peek, it is O(n) in the worst case.
- The space complexity is O(n) where n is the number of elements in the queue.