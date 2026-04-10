# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The stack is empty if both queues are empty. The problem requires designing a class that supports these operations efficiently.

## Approach
We can implement a stack using two queues by utilizing the queue's FIFO property to mimic the LIFO behavior of a stack. When pushing an element, we add it to the end of the first queue. When popping an element, we move all elements except the last one from the first queue to the second queue, then remove the last element from the first queue.

## Complexity
- Time: O(n) for pop operation (where n is the number of elements in the stack), O(1) for push operation
- Space: O(n) (where n is the total number of elements in the stack)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MyStack {
private:
    queue<int> q1;
    queue<int> q2;
public:
    // Push element x onto stack
    void push(int x) {
        q1.push(x);
    }

    // Removes the element on top of the stack
    void pop() {
        if (q1.empty()) return;
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        q1.pop();
        swap(q1, q2);
    }

    // Get the top element
    int top() {
        if (q1.empty()) return -1;
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        int topElement = q1.front();
        q2.push(q1.front());
        q1.pop();
        swap(q1, q2);
        return topElement;
    }

    // Return whether the stack is empty
    bool empty() {
        return q1.empty() && q2.empty();
    }
};
```

## Test Cases
```
Input: MyStack stack = new MyStack();
       stack.push(1);
       stack.push(2);
       stack.push(3);
       stack.pop();
       stack.pop();
       stack.pop();
Output: 
       // top after push 1: 1
       // top after push 2: 2
       // top after push 3: 3
       // after pop: 3
       // after pop: 2
       // after pop: 1
       // stack is empty
```

## Key Takeaways
- Use two queues to implement a stack, with one queue always containing the top element of the stack.
- The push operation is O(1), while the pop operation is O(n) in the worst case.
- The space complexity is O(n), where n is the number of elements in the stack.