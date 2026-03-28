# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added to the queue will be the first one to be removed. The queue should support the following operations: `push(x)`, `pop()`, `peek()`, and `empty()`. The `push(x)` operation adds an element `x` to the end of the queue. The `pop()` operation removes the front element from the queue and returns it. The `peek()` operation returns the front element of the queue without removing it. The `empty()` operation checks whether the queue is empty.

## Approach
We can implement a queue using two stacks by using one stack for enqueue operations and the other stack for dequeue operations. When an element is added to the queue, it is pushed onto the first stack. When an element is removed from the queue, the elements are popped from the first stack and pushed onto the second stack, effectively reversing the order of the elements.

## Complexity
- Time: O(1) for `push(x)` and `empty()`, O(n) for `pop()` and `peek()` in the worst case
- Space: O(n) where n is the number of elements in the queue

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

    // Removes the element from the front of queue.
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
       cout << queue.peek() << endl;  // Output: 1
       cout << queue.pop() << endl;    // Output: 1
       cout << queue.empty() << endl;  // Output: 0
```

## Key Takeaways
- We use two stacks, `s1` and `s2`, to implement the queue.
- The `push(x)` operation is implemented by pushing the element onto `s1`.
- The `pop()` and `peek()` operations are implemented by popping the elements from `s1` and pushing them onto `s2` when `s2` is empty, effectively reversing the order of the elements.