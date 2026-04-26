# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard stack operations: push, pop, top, and empty. The push operation adds an element to the top of the stack, the pop operation removes the top element from the stack, the top operation returns the top element of the stack without removing it, and the empty operation checks if the stack is empty. The stack should be implemented using only two queues, and the operations should be performed efficiently.

## Approach
We can implement a stack using two queues by using one queue as the main stack and the other queue as a temporary buffer. When pushing an element, we add it to the main queue. When popping an element, we move all elements except the last one from the main queue to the temporary queue, then remove the last element from the main queue.

## Complexity
- Time: O(1) for push, O(n) for pop and top, where n is the number of elements in the stack
- Space: O(n), where n is the number of elements in the stack

## C++ Solution
```cpp
#include <queue>
using namespace std;

class MyStack {
private:
    queue<int> q1;
    queue<int> q2;
public:
    MyStack() {}

    void push(int x) {
        q2.push(x);
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }
        swap(q1, q2);
    }

    int pop() {
        if (q1.empty()) {
            return -1; // or throw an exception
        }
        int top = q1.front();
        q1.pop();
        return top;
    }

    int top() {
        if (q1.empty()) {
            return -1; // or throw an exception
        }
        return q1.front();
    }

    bool empty() {
        return q1.empty();
    }
};
```

## Test Cases
```
Input: MyStack stack; stack.push(1); stack.push(2); stack.push(3); stack.pop(); stack.top();
Output: 2
```

## Key Takeaways
- We use two queues to implement a stack, with one queue as the main stack and the other queue as a temporary buffer.
- The push operation adds an element to the top of the stack by moving all elements from the main queue to the temporary queue, then adding the new element to the temporary queue, and finally swapping the two queues.
- The pop and top operations are performed by removing or accessing the front element of the main queue.