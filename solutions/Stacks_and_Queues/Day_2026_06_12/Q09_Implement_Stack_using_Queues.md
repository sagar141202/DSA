# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The constraints are that we can only use two queues to implement the stack, and we cannot use any other data structures. For example, if we push the elements 1, 2, and 3 onto the stack, the top of the stack should be 3, and popping from the stack should return 3, then 2, then 1.

## Approach
We can implement a stack using two queues by using one queue as the main stack and the other queue as a temporary buffer. When pushing an element, we add it to the end of the main queue. When popping an element, we move all elements except the last one from the main queue to the temporary queue, then remove and return the last element from the main queue.

## Complexity
- Time: O(n) for pop operation, O(1) for push operation
- Space: O(n)

## C++ Solution
```cpp
#include <queue>
using namespace std;

class Stack {
private:
    queue<int> q1;
    queue<int> q2;

public:
    void push(int x) {
        q2.push(x);
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }
        swap(q1, q2);
    }

    int pop() {
        if (q1.empty()) {
            return -1; // or throw an exception
        }
        int top = q1.front();
        q1.pop();
        return top;
    }

    int top() {
        if (q1.empty()) {
            return -1; // or throw an exception
        }
        return q1.front();
    }

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
- We use two queues to implement a stack, with one queue serving as the main stack and the other as a temporary buffer.
- The push operation adds an element to the end of the main queue, while the pop operation removes an element from the front of the main queue.
- The time complexity of the push operation is O(1) and the time complexity of the pop operation is O(n), where n is the number of elements in the stack.