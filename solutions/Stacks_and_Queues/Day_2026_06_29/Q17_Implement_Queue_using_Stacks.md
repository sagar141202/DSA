# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added to the queue will be the first one to be removed. The queue should support the following operations: `enqueue(x)`, which adds an element `x` to the end of the queue, `dequeue()`, which removes an element from the front of the queue, and `empty()`, which checks if the queue is empty. The input will be a sequence of these operations, and the output should be the result of each `dequeue` operation.

## Approach
We will use two stacks to implement the queue. The first stack will be used to store the elements in the order they are added, and the second stack will be used to reverse the order of the elements when an element is removed. When an element is added, it will be pushed onto the first stack. When an element is removed, the elements will be popped from the first stack and pushed onto the second stack until the first stack is empty, then the top element of the second stack will be popped and returned.

## Complexity
- Time: O(1) for `enqueue` and `empty` operations, and O(n) for `dequeue` operation in the worst case, where n is the number of elements in the queue.
- Space: O(n), where n is the number of elements in the queue.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MyQueue {
private:
    stack<int> s1; // stack to store elements in the order they are added
    stack<int> s2; // stack to store elements in the reverse order

public:
    // Push element x to the back of queue.
    void push(int x) {
        s1.push(x);
    }

    // Removes the element from in front of queue.
    int pop() {
        if (s2.empty()) {
            // if s2 is empty, move elements from s1 to s2
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
            // if s2 is empty, move elements from s1 to s2
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        return s2.top();
    }

    // Returns whether the queue is empty.
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
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
```

## Key Takeaways
- We can use two stacks to implement a queue, with one stack storing elements in the order they are added and the other stack storing elements in the reverse order.
- The `dequeue` operation has a time complexity of O(n) in the worst case, where n is the number of elements in the queue.
- The `enqueue` and `empty` operations have a time complexity of O(1).