# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added will be the first one to be removed. The queue should support the following operations: `push(x)` - Push element x to the back of queue, `pop()` - Removes the element from the front of queue, `peek()` - Get the front element, `empty()` - Return whether the queue is empty. The input will be a series of these operations. The constraints are that 1 <= x <= 10^9 and at most 100 operations will be performed.

## Approach
We can use two stacks to implement a queue. One stack will be used to store new elements and the other stack will be used to store elements in the correct order for removal. When an element is added, it will be pushed onto the first stack. When an element is removed, if the second stack is empty, we will pop all elements from the first stack and push them onto the second stack. Then we can pop the top element from the second stack.

## Complexity
- Time: O(1) amortized for push and peek, O(n) in the worst case for pop
- Space: O(n)

## C++ Solution
```cpp
#include <stack>

class MyQueue {
public:
    std::stack<int> stackNewestOnTop; // stack to store new elements
    std::stack<int> stackOldestOnTop; // stack to store elements in the correct order for removal

    MyQueue() {}

    void push(int x) {
        // Push element x onto the stack of new elements
        stackNewestOnTop.push(x);
    }

    int pop() {
        // If the stack of old elements is empty, move elements from the new stack to the old stack
        if (stackOldestOnTop.empty()) {
            while (!stackNewestOnTop.empty()) {
                stackOldestOnTop.push(stackNewestOnTop.top());
                stackNewestOnTop.pop();
            }
        }
        // Pop the top element from the stack of old elements
        int top = stackOldestOnTop.top();
        stackOldestOnTop.pop();
        return top;
    }

    int peek() {
        // If the stack of old elements is empty, move elements from the new stack to the old stack
        if (stackOldestOnTop.empty()) {
            while (!stackNewestOnTop.empty()) {
                stackOldestOnTop.push(stackNewestOnTop.top());
                stackNewestOnTop.pop();
            }
        }
        // Return the top element from the stack of old elements
        return stackOldestOnTop.top();
    }

    bool empty() {
        // Return whether both stacks are empty
        return stackNewestOnTop.empty() && stackOldestOnTop.empty();
    }
};
```

## Test Cases
```
Input: MyQueue queue; queue.push(1); queue.push(2); queue.peek(); queue.pop(); queue.empty()
Output: 1, 1, false
```

## Key Takeaways
- We can implement a queue using two stacks by using one stack to store new elements and the other stack to store elements in the correct order for removal.
- The time complexity for push and peek operations is O(1) amortized, but can be O(n) in the worst case for pop operations.
- The space complexity is O(n), where n is the number of elements in the queue.