# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element that is added will be the first one to be removed. The queue should support the following operations: `enqueue(x)`, which adds an element `x` to the end of the queue, and `dequeue()`, which removes an element from the front of the queue. The queue should also support `isEmpty()`, which checks if the queue is empty, and `size()`, which returns the number of elements in the queue. For example, if we `enqueue(1)`, `enqueue(2)`, and `enqueue(3)`, then `dequeue()` should return `1`, `dequeue()` should return `2`, and `dequeue()` should return `3`.

## Approach
We can implement a queue using two stacks by using one stack for enqueue operations and the other stack for dequeue operations. When an element is enqueued, it is pushed onto the first stack. When an element is dequeued, we pop all elements from the first stack and push them onto the second stack, then pop the top element from the second stack.

## Complexity
- Time: O(1) for enqueue, O(n) for dequeue in the worst case
- Space: O(n), where n is the number of elements in the queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Queue {
private:
    stack<int> s1;
    stack<int> s2;

public:
    // Add an element to the queue
    void enqueue(int x) {
        s1.push(x);
    }

    // Remove an element from the queue
    int dequeue() {
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

    // Check if the queue is empty
    bool isEmpty() {
        return s1.empty() && s2.empty();
    }

    // Get the size of the queue
    int size() {
        return s1.size() + s2.size();
    }
};
```

## Test Cases
```
Input: 
enqueue(1)
enqueue(2)
enqueue(3)
dequeue()
dequeue()
dequeue()
isEmpty()
size()
Output: 
1
2
3
true
0
```

## Key Takeaways
- We can implement a queue using two stacks by using one stack for enqueue operations and the other stack for dequeue operations.
- The time complexity of enqueue is O(1), while the time complexity of dequeue is O(n) in the worst case.
- The space complexity of the queue is O(n), where n is the number of elements in the queue.