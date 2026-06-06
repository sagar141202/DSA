# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes the top element from the stack. Given two queues, q1 and q2, we need to implement the stack operations using these queues. The constraints are that we can only use the standard queue operations (enqueue, dequeue, and size) to implement the stack. For example, if we push the elements 1, 2, and 3 into the stack, the top of the stack should be 3, and after popping, the top of the stack should be 2.

## Approach
We will use two queues to implement the stack. The first queue (q1) will store the actual stack elements, and the second queue (q2) will be used as a temporary queue to help with the pop operation. When we push an element into the stack, we will simply enqueue it into q1. When we pop an element from the stack, we will dequeue all elements from q1 except the last one and enqueue them into q2, then dequeue the last element from q1 (which is the top of the stack), and finally swap q1 and q2.

## Complexity
- Time: O(n) for pop operation, O(1) for push operation
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Stack {
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
        if (q1.empty()) {
            return;
        }
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        q1.pop();
        queue<int> temp = q1;
        q1 = q2;
        q2 = temp;
    }

    // Get the top element
    int top() {
        if (q1.empty()) {
            return -1; // or throw an exception
        }
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        int topElement = q1.front();
        q2.push(q1.front());
        q1.pop();
        queue<int> temp = q1;
        q1 = q2;
        q2 = temp;
        return topElement;
    }

    // Return whether the stack is empty
    bool empty() {
        return q1.empty();
    }
};

int main() {
    Stack stack;
    stack.push(1);
    stack.push(2);
    stack.push(3);
    cout << stack.top() << endl; // prints 3
    stack.pop();
    cout << stack.top() << endl; // prints 2
    return 0;
}
```

## Test Cases
```
Input: push(1), push(2), push(3), top(), pop(), top()
Output: 3, 2
```

## Key Takeaways
- We can implement a stack using two queues by using one queue as the main stack and the other as a temporary queue for the pop operation.
- The time complexity of the pop operation is O(n) because we need to dequeue all elements from the main queue except the last one, while the time complexity of the push operation is O(1) because we simply enqueue the element into the main queue.