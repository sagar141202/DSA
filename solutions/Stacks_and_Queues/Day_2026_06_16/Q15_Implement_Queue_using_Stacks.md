# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added to the queue will be the first one to be removed. The queue should support the following operations: `enqueue`, `dequeue`, and `isEmpty`. The `enqueue` operation adds an element to the end of the queue, the `dequeue` operation removes an element from the front of the queue, and the `isEmpty` operation checks if the queue is empty. The input will be a series of operations, where each operation is either `enqueue x` or `dequeue`. The output should be the result of each `dequeue` operation.

## Approach
We can implement a queue using two stacks by using one stack for enqueue operations and the other stack for dequeue operations. When we need to dequeue an element, we can pop all elements from the enqueue stack and push them onto the dequeue stack, then pop the top element from the dequeue stack.

## Complexity
- Time: O(1) for enqueue, O(n) for dequeue in the worst case
- Space: O(n), where n is the number of elements in the queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MyQueue {
private:
    stack<int> stack1; // enqueue stack
    stack<int> stack2; // dequeue stack

public:
    // enqueue operation
    void enqueue(int x) {
        stack1.push(x);
    }

    // dequeue operation
    int dequeue() {
        if (stack2.empty()) {
            // if dequeue stack is empty, pop all elements from enqueue stack and push them onto dequeue stack
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        int top = stack2.top();
        stack2.pop();
        return top;
    }

    // check if queue is empty
    bool isEmpty() {
        return stack1.empty() && stack2.empty();
    }
};

int main() {
    MyQueue queue;
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    cout << queue.dequeue() << endl; // output: 1
    cout << queue.dequeue() << endl; // output: 2
    cout << queue.isEmpty() << endl; // output: 0
    return 0;
}
```

## Test Cases
```
Input: enqueue 1, enqueue 2, enqueue 3, dequeue, dequeue, isEmpty
Output: 1, 2, 0
```

## Key Takeaways
- We can implement a queue using two stacks by using one stack for enqueue operations and the other stack for dequeue operations.
- The time complexity of enqueue operation is O(1), and the time complexity of dequeue operation is O(n) in the worst case.
- The space complexity is O(n), where n is the number of elements in the queue.