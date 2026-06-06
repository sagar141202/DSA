# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added to the queue will be the first one to be removed. The queue should support the following operations: `push(x)` - Push element x to the back of queue, `pop()` - Removes the element from the front of queue, `peek()` - Get the front element, `empty()` - Return whether the queue is empty. The input will be a sequence of these operations. For example, given the operations `push(1)`, `push(2)`, `peek()`, `pop()`, `empty()`, the output should be `1`, `1`. The queue will be empty after the `pop()` operation.

## Approach
We can implement a queue using two stacks by using one stack for enqueue operations and the other stack for dequeue operations. When an element is pushed into the queue, it is pushed into the first stack. When an element is popped from the queue, we pop all elements from the first stack and push them into the second stack, then pop the top element from the second stack.

## Complexity
- Time: O(1) for `push(x)`, `peek()`, `empty()` operations, O(n) for `pop()` operation in the worst case where n is the number of elements in the queue.
- Space: O(n) where n is the number of elements in the queue.

## C++ Solution
```cpp
#include <stack>
using namespace std;

class MyQueue {
private:
    stack<int> s1;
    stack<int> s2;

public:
    // Push element x to the back of queue.
    void push(int x) {
        // Simply push the element into the first stack.
        s1.push(x);
    }

    // Removes the element from the front of queue.
    int pop() {
        // If the second stack is empty, we need to move all elements from the first stack to the second stack.
        if (s2.empty()) {
            while (!s1.empty()) {
                // Pop the top element from the first stack and push it into the second stack.
                s2.push(s1.top());
                s1.pop();
            }
        }
        // Pop the top element from the second stack.
        int top = s2.top();
        s2.pop();
        return top;
    }

    // Get the front element.
    int peek() {
        // If the second stack is empty, we need to move all elements from the first stack to the second stack.
        if (s2.empty()) {
            while (!s1.empty()) {
                // Pop the top element from the first stack and push it into the second stack.
                s2.push(s1.top());
                s1.pop();
            }
        }
        // Return the top element from the second stack.
        return s2.top();
    }

    // Return whether the queue is empty.
    bool empty() {
        // The queue is empty if both stacks are empty.
        return s1.empty() && s2.empty();
    }
};
```

## Test Cases
```
Input: MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
print(queue.peek()); // Output: 1
print(queue.pop());  // Output: 1
print(queue.empty()); // Output: false
```

## Key Takeaways
- We use two stacks to implement a queue, one for enqueue operations and the other for dequeue operations.
- The `pop()` and `peek()` operations have a worst-case time complexity of O(n) where n is the number of elements in the queue.
- We can optimize the `pop()` and `peek()` operations by moving elements from the first stack to the second stack only when necessary.