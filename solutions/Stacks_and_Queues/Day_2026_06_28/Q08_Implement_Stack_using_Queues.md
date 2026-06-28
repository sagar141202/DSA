# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard stack operations: push, pop, top, and isEmpty. The push operation adds an element to the top of the stack, the pop operation removes an element from the top of the stack, the top operation returns the element at the top of the stack without removing it, and the isEmpty operation checks if the stack is empty. The input will be a sequence of these operations. The output should be the result of each operation.

## Approach
We can implement a stack using two queues by using one queue as the main stack and the other queue as a temporary buffer. When an element is pushed, it is added to the main queue. When an element is popped, all elements except the last one are moved to the temporary queue, and then the last element is removed from the main queue. The top operation can be implemented similarly by moving all elements except the last one to the temporary queue and then returning the last element.

## Complexity
- Time: O(n) for pop and top operations, O(1) for push and isEmpty operations
- Space: O(n)

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
        if (q1.empty()) return;
        q1.pop();
    }

    // Get the top element
    int top() {
        if (q1.empty()) return -1;
        return q1.front();
    }

    // Return whether the stack is empty
    bool empty() {
        return q1.empty();
    }
};
```

## Test Cases
```
Input: push(1), push(2), top(), pop(), empty()
Output: 2, true
```

## Key Takeaways
- We use two queues to implement a stack.
- The push operation has a time complexity of O(n) because we are adding an element to the end of the queue.
- The pop and top operations have a time complexity of O(n) because we are removing an element from the front of the queue.
- The isEmpty operation has a time complexity of O(1) because we are simply checking if the queue is empty.