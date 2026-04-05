# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added will be the first one to be removed. Given two stacks, `stack1` and `stack2`, implement the `enqueue` and `dequeue` operations. The `enqueue` operation adds an element to the end of the queue, while the `dequeue` operation removes an element from the front of the queue. The queue should support the following operations: `enqueue(x)`, `dequeue()`, `isEmpty()`, and `size()`. The input will be a series of operations, and the output will be the result of each operation.

## Approach
We can implement a queue using two stacks by using one stack for enqueue operations and the other stack for dequeue operations. When an element is enqueued, it is pushed onto the first stack. When an element is dequeued, we pop all elements from the first stack and push them onto the second stack, then pop the top element from the second stack.

## Complexity
- Time: O(1) for enqueue, O(n) for dequeue (amortized O(1))
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Queue {
private:
    stack<int> stack1;
    stack<int> stack2;

public:
    // Add an element to the queue
    void enqueue(int x) {
        stack1.push(x);
    }

    // Remove an element from the queue
    int dequeue() {
        if (stack2.empty()) {
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        if (stack2.empty()) {
            throw runtime_error("Queue is empty");
        }
        int x = stack2.top();
        stack2.pop();
        return x;
    }

    // Check if the queue is empty
    bool isEmpty() {
        return stack1.empty() && stack2.empty();
    }

    // Get the size of the queue
    int size() {
        return stack1.size() + stack2.size();
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
isEmpty()
size()

Output: 
1
2
false
1
```

## Key Takeaways
- We can use two stacks to implement a queue by using one stack for enqueue operations and the other stack for dequeue operations.
- The time complexity of the enqueue operation is O(1), while the time complexity of the dequeue operation is O(n) in the worst case, but amortized O(1) over a sequence of operations.
- The space complexity of the queue is O(n), where n is the number of elements in the queue.