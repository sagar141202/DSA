# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added will be the first one to be removed. The queue should support the following operations: `push(x)`, `pop()`, `peek()`, `empty()`. The `push(x)` operation adds an element to the end of the queue. The `pop()` operation removes an element from the front of the queue. The `peek()` operation returns the element at the front of the queue without removing it. The `empty()` operation checks if the queue is empty.

## Approach
We will use two stacks to implement the queue. The first stack will be used to add elements to the queue, and the second stack will be used to remove elements from the queue. When an element is added to the queue, it will be pushed onto the first stack. When an element is removed from the queue, it will be popped from the second stack. If the second stack is empty, we will transfer all elements from the first stack to the second stack.

## Complexity
- Time: O(1) for push, O(1) for pop and peek when the second stack is not empty, O(n) for pop and peek when the second stack is empty
- Space: O(n)

## C++ Solution
```cpp
#include <stack>

class MyQueue {
private:
    std::stack<int> stack1;
    std::stack<int> stack2;

public:
    // Push element x to the back of queue.
    void push(int x) {
        stack1.push(x);
    }

    // Removes the element from the front of queue and returns it.
    int pop() {
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

    // Get the front element.
    int peek() {
        if (stack2.empty()) {
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        return stack2.top();
    }

    // Returns whether the queue is empty.
    bool empty() {
        return stack1.empty() && stack2.empty();
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
- A queue can be implemented using two stacks.
- The time complexity of push operation is O(1), while the time complexity of pop and peek operations can be O(1) or O(n) depending on whether the second stack is empty.
- The space complexity is O(n), where n is the number of elements in the queue.