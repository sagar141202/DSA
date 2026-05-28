# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added to the queue will be the first one to be removed. The queue should support the following operations: `enqueue` (add an element to the end of the queue), `dequeue` (remove an element from the front of the queue), `peek` (return the element at the front of the queue without removing it), and `isEmpty` (check if the queue is empty). The input will be a sequence of these operations, and the output should be the result of each operation.

## Approach
We will use two stacks to implement the queue. The first stack will be used to store the elements in the order they are added, and the second stack will be used to store the elements in the reverse order. When an element is added to the queue, it will be pushed onto the first stack. When an element is removed from the queue, it will be popped from the second stack if it is not empty, or the elements will be transferred from the first stack to the second stack and then popped.

## Complexity
- Time: O(1) for enqueue, O(1) for dequeue (amortized), O(1) for peek, O(1) for isEmpty
- Space: O(n), where n is the number of elements in the queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MyQueue {
private:
    stack<int> s1; // stack for enqueue
    stack<int> s2; // stack for dequeue

public:
    // Push element x to the back of queue.
    void push(int x) {
        s1.push(x);
    }

    // Removes the element from in front of queue.
    int pop() {
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        int top = s2.top();
        s2.pop();
        return top;
    }

    // Get the front element.
    int peek() {
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        return s2.top();
    }

    // Return whether the queue is empty.
    bool empty() {
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
- We can use two stacks to implement a queue, where one stack is used for enqueue and the other stack is used for dequeue.
- The time complexity for enqueue is O(1), and the time complexity for dequeue is O(1) amortized.
- The space complexity is O(n), where n is the number of elements in the queue.