# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added will be the first one to be removed. The queue should support the following operations: `push(x)` - Push element x to the back of queue, `pop()` - Removes the element from the front of queue, `peek()` - Get the front element, `empty()` - Return whether the queue is empty. The input will be a series of operations, and the output should be the result of each operation.

## Approach
We will use two stacks to implement the queue. The first stack will be used to store the incoming elements, and the second stack will be used to store the elements in the correct order for removal. When an element is added, it will be pushed onto the first stack. When an element is removed, it will be popped from the second stack if it is not empty, otherwise the elements will be transferred from the first stack to the second stack.

## Complexity
- Time: O(1) amortized for push and peek, O(n) in the worst case for pop
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
            throw std::runtime_error("Queue is empty");
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
            throw std::runtime_error("Queue is empty");
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
Input: MyQueue queue; queue.push(1); queue.push(2); queue.peek(); queue.pop(); queue.empty();
Output: 1, 1, false
```

## Key Takeaways
- We use two stacks to implement a queue, one for adding elements and one for removing elements.
- The `pop` and `peek` operations have an amortized time complexity of O(1), but can be O(n) in the worst case when the second stack is empty.
- The `push` operation always has a time complexity of O(1).