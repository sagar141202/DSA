# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element that is added will be the first one to be removed. The queue should support the following operations: `push(x)`, `pop()`, `peek()`, `empty()`. The `push(x)` operation adds an element `x` to the end of the queue. The `pop()` operation removes the element from the front of the queue. The `peek()` operation returns the element from the front of the queue without removing it. The `empty()` operation checks if the queue is empty.

## Approach
We can use two stacks to implement a queue. The first stack will be used to store new elements and the second stack will be used to store the elements in the correct order. When an element is added to the queue, it will be pushed onto the first stack. When an element is removed from the queue, we will pop all elements from the first stack and push them onto the second stack, then pop the top element from the second stack.

## Complexity
- Time: O(1) for `push(x)` and `empty()`, amortized O(1) for `pop()` and `peek()`
- Space: O(n), where n is the number of elements in the queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MyQueue {
private:
    stack<int> s1, s2;
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
        int temp = s2.top();
        s2.pop();
        return temp;
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
- We can use two stacks to implement a queue, one for storing new elements and one for storing elements in the correct order.
- The `push(x)` operation has a time complexity of O(1) because we simply push the element onto the first stack.
- The `pop()` and `peek()` operations have an amortized time complexity of O(1) because we only need to pop all elements from the first stack and push them onto the second stack when the second stack is empty.