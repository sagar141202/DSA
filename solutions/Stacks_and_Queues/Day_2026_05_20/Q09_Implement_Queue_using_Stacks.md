# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added to the queue will be the first one to be removed. The queue should support the following operations: `push(x)`, `pop()`, `peek()`, `empty()`. The `push(x)` operation adds an element `x` to the end of the queue. The `pop()` operation removes the element from the front of the queue. The `peek()` operation returns the element at the front of the queue without removing it. The `empty()` operation checks if the queue is empty.

## Approach
We will use two stacks to implement the queue. The first stack will be used to store the elements in the order they are added, and the second stack will be used to store the elements in the reverse order. When an element is added to the queue, it will be pushed onto the first stack. When an element is removed from the queue, it will be popped from the second stack. If the second stack is empty, the elements from the first stack will be transferred to the second stack.

## Complexity
- Time: O(1) for push, O(1) for pop and peek when the second stack is not empty, O(n) for pop and peek when the second stack is empty
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MyQueue {
private:
    stack<int> s1;
    stack<int> s2;

public:
    // Push element x to the back of queue
    void push(int x) {
        // Push the element onto the first stack
        s1.push(x);
    }

    // Removes the element from the front of queue
    int pop() {
        // If the second stack is empty, transfer elements from the first stack
        if (s2.empty()) {
            while (!s1.empty()) {
                // Pop the element from the first stack and push it onto the second stack
                s2.push(s1.top());
                s1.pop();
            }
        }
        // Pop the element from the second stack
        int temp = s2.top();
        s2.pop();
        return temp;
    }

    // Get the front element
    int peek() {
        // If the second stack is empty, transfer elements from the first stack
        if (s2.empty()) {
            while (!s1.empty()) {
                // Pop the element from the first stack and push it onto the second stack
                s2.push(s1.top());
                s1.pop();
            }
        }
        // Return the top element of the second stack
        return s2.top();
    }

    // Return whether the queue is empty
    bool empty() {
        // Check if both stacks are empty
        return s1.empty() && s2.empty();
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
- We can use two stacks to implement a queue, where the first stack stores the elements in the order they are added and the second stack stores the elements in the reverse order.
- The `push` operation has a time complexity of O(1), while the `pop` and `peek` operations have a time complexity of O(1) when the second stack is not empty and O(n) when the second stack is empty.
- The space complexity of the implementation is O(n), where n is the number of elements in the queue.