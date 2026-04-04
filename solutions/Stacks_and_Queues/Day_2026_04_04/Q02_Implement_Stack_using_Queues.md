# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the basic operations: push, pop, and top. The push operation adds an element to the top of the stack, the pop operation removes the top element from the stack, and the top operation returns the top element of the stack without removing it. The queues should be used as the underlying data structure to implement the stack. The constraints are that we can only use two queues and the standard queue operations (enqueue, dequeue, and isEmpty).

## Approach
We can implement a stack using two queues by using one queue as the main stack and the other queue as a temporary queue to hold the elements when we need to add or remove an element from the top of the stack. We will use the enqueue and dequeue operations to add and remove elements from the queues.

## Complexity
- Time: O(1) for push, O(n) for pop and top in the worst case
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
    /** Push element x onto stack. */
    void push(int x) {
        q2.push(x);
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }
        swap(q1, q2);
    }

    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        if (q1.empty()) {
            return -1; // or throw an exception
        }
        int top = q1.front();
        q1.pop();
        return top;
    }

    /** Get the top element. */
    int top() {
        if (q1.empty()) {
            return -1; // or throw an exception
        }
        return q1.front();
    }

    /** Returns whether the stack is empty. */
    bool empty() {
        return q1.empty();
    }
};
```

## Test Cases
```
Input: push(1), push(2), pop(), top()
Output: 2, 1
Input: push(1), pop(), empty()
Output: 1, true
```

## Key Takeaways
- We can use two queues to implement a stack by using one queue as the main stack and the other queue as a temporary queue.
- The push operation takes O(n) time in the worst case because we need to move all elements from the main queue to the temporary queue.
- The pop and top operations take O(1) time because we can directly access the front element of the main queue.