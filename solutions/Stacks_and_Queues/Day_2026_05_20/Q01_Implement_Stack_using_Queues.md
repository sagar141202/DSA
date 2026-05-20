# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should have the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The queue operations allowed are enqueue and dequeue. For example, if we push elements 1, 2, and 3 into the stack, the top of the stack should be 3, and after popping, the top of the stack should be 2.

## Approach
We can use two queues to implement a stack. One queue will store the actual elements, and the other queue will be used to reverse the order of elements when pushing a new element. The algorithm works by enqueueing the new element into the second queue, then dequeuing all elements from the first queue and enqueueing them into the second queue, effectively reversing the order.

## Complexity
- Time: O(n) for push operation, O(1) for pop operation (amortized)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Stack {
private:
    queue<int> q1, q2;
public:
    void push(int x) {
        // Enqueue new element into q2
        q2.push(x);
        // Dequeue all elements from q1 and enqueue them into q2
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }
        // Swap q1 and q2
        swap(q1, q2);
    }

    int pop() {
        // Check if the stack is empty
        if (q1.empty()) {
            return -1; // or throw an exception
        }
        // Dequeue the front element from q1
        int front = q1.front();
        q1.pop();
        return front;
    }

    int top() {
        // Check if the stack is empty
        if (q1.empty()) {
            return -1; // or throw an exception
        }
        // Return the front element from q1
        return q1.front();
    }
};
```

## Test Cases
```
Input: push(1), push(2), push(3), pop()
Output: 3
Input: top()
Output: 2
```

## Key Takeaways
- We can use two queues to implement a stack with push and pop operations.
- The push operation has an amortized time complexity of O(1) because we only need to reverse the order of elements when pushing a new element.
- The space complexity is O(n) where n is the number of elements in the stack.