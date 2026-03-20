# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. A stack is a linear data structure that follows the LIFO (Last In First Out) principle, whereas a queue is a linear data structure that follows the FIFO (First In First Out) principle. The stack should support the following operations: push, pop, top, and empty. The push operation adds an element to the top of the stack, the pop operation removes the top element from the stack, the top operation returns the top element of the stack, and the empty operation checks if the stack is empty. The input will be a sequence of these operations, and the output will be the result of each operation.

## Approach
We can implement a stack using two queues by using one queue as the main stack and the other queue as a temporary queue. When pushing an element, we add it to the main queue. When popping an element, we move all elements except the last one from the main queue to the temporary queue, then remove the last element from the main queue. When getting the top element, we move all elements except the last one from the main queue to the temporary queue, then return the last element from the main queue without removing it.

## Complexity
- Time: O(n) for pop and top operations, O(1) for push and empty operations
- Space: O(n) for storing the elements in the queues

## C++ Solution
```cpp
#include <queue>
using namespace std;

class MyStack {
private:
    queue<int> q1;
    queue<int> q2;
public:
    // Push element x onto stack
    void push(int x) {
        q2.push(x);
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }
        swap(q1, q2);
    }

    // Removes the element on top of the stack
    void pop() {
        if (!q1.empty()) {
            q1.pop();
        }
    }

    // Get the top element
    int top() {
        if (!q1.empty()) {
            return q1.front();
        }
        return -1; // or throw an exception
    }

    // Return whether the stack is empty
    bool empty() {
        return q1.empty();
    }
};
```

## Test Cases
```
Input: ["MyStack", "push", "push", "top", "pop", "empty"]
Output: [null, null, null, 2, null, false]
Input: ["MyStack", "push", "push", "pop", "pop", "empty"]
Output: [null, null, null, null, null, true]
```

## Key Takeaways
- We use two queues to implement a stack, one as the main stack and the other as a temporary queue.
- The push operation adds an element to the top of the stack by adding it to the temporary queue and then swapping the queues.
- The pop operation removes the top element from the stack by removing the front element from the main queue.