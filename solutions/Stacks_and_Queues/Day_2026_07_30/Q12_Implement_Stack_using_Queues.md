# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The stack should be empty initially, and the pop operation should return -1 if the stack is empty. For example, if we push the elements 1, 2, and 3 in that order, the stack should contain the elements [3, 2, 1] from top to bottom. If we then pop an element, the stack should contain [2, 1] and the popped element should be 3.

## Approach
We can implement a stack using two queues by using one queue to store the elements and the other queue to help with the pop operation. When an element is pushed, we add it to the end of the first queue. When an element is popped, we remove the front element from the first queue and add all the remaining elements to the second queue, then swap the two queues.

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
    int pop() {
        if (q1.empty()) {
            return -1;
        }
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        int top = q1.front();
        q1.pop();
        swap(q1, q2);
        return top;
    }

    // Get the top element
    int top() {
        if (q1.empty()) {
            return -1;
        }
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        int top = q1.front();
        q2.push(q1.front());
        q1.pop();
        swap(q1, q2);
        return top;
    }

    // Return whether the stack is empty
    bool empty() {
        return q1.empty();
    }
};
```

## Test Cases
```
Input: push(1), push(2), push(3), pop(), top()
Output: 3, 2
```

## Key Takeaways
- We can implement a stack using two queues by using one queue to store the elements and the other queue to help with the pop operation.
- The pop operation takes O(n) time because we need to remove the front element from the first queue and add all the remaining elements to the second queue.
- The push operation takes O(1) time because we simply add the element to the end of the first queue.