# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the following operations: push, pop, top, and isEmpty. The push operation adds an element to the top of the stack, the pop operation removes the top element from the stack, the top operation returns the top element of the stack, and the isEmpty operation checks if the stack is empty. The stack should be implemented using only two queues.

## Approach
We can implement a stack using two queues by using one queue for storing the elements and the other queue for temporary storage during the pop operation. When an element is pushed, it is added to the first queue. When an element is popped, we move all elements except the last one from the first queue to the second queue, and then remove the last element from the first queue.

## Complexity
- Time: O(n) for pop operation, O(1) for push, top, and isEmpty operations
- Space: O(n) where n is the number of elements in the stack

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
Input: push(1), push(2), push(3), pop(), top(), isEmpty()
Output: 3, 2, false
```

## Key Takeaways
- We can implement a stack using two queues by using one queue for storing the elements and the other queue for temporary storage during the pop operation.
- The time complexity of the pop operation is O(n) because we need to move all elements from one queue to another.
- The space complexity is O(n) where n is the number of elements in the stack.