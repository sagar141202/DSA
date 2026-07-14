# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The problem constraints are that we can only use queues to implement the stack, and we should minimize the time complexity of the push and pop operations. For example, if we push the elements 1, 2, and 3 onto the stack, the top element should be 3, and popping from the stack should return 3, then 2, then 1.

## Approach
We will use two queues, q1 and q2, to implement the stack. The push operation will add an element to the end of q1. The pop operation will remove the front element from q1, which will be the top element of the stack. To achieve this, we will move all elements except the front one from q1 to q2, then dequeue the front element from q1, and finally swap q1 and q2.

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
    // Push element x onto stack
    void push(int x) {
        q1.push(x);
    }

    // Removes the element on top of the stack
    void pop() {
        if (q1.empty()) return;
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        q1.pop();
        swap(q1, q2);
    }

    // Get the top element
    int top() {
        if (q1.empty()) return -1;
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        int topElement = q1.front();
        q2.push(q1.front());
        q1.pop();
        swap(q1, q2);
        return topElement;
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
- We can implement a stack using two queues by moving elements between the queues to maintain the stack order.
- The time complexity of the push operation is O(1), while the time complexity of the pop operation is O(n) due to the need to move elements between the queues.
- The space complexity is O(n), where n is the number of elements in the stack.