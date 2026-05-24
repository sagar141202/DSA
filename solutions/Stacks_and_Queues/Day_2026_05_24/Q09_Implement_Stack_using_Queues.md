# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The problem constraints are that we can only use two queues to implement the stack, and we cannot use any other data structures. For example, if we push the elements 1, 2, and 3 onto the stack, the top element should be 3, and popping the stack should return 3. If we then push the element 4 onto the stack, the top element should be 4.

## Approach
We will use two queues, q1 and q2, to implement the stack. When pushing an element, we will add it to the end of q1. When popping an element, we will move all elements from q1 to q2 except the last one, which will be the top element of the stack.

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
        // Add the element to the end of q1
        q1.push(x);
    }

    int pop() {
        // Check if the stack is empty
        if (q1.empty()) {
            throw runtime_error("Stack is empty");
        }

        // Move all elements from q1 to q2 except the last one
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }

        // The last element in q1 is the top of the stack
        int top = q1.front();
        q1.pop();

        // Swap q1 and q2
        swap(q1, q2);

        return top;
    }

    int top() {
        // Check if the stack is empty
        if (q1.empty()) {
            throw runtime_error("Stack is empty");
        }

        // Move all elements from q1 to q2 except the last one
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }

        // The last element in q1 is the top of the stack
        int top = q1.front();
        q1.pop();

        // Add the top element back to q2
        q2.push(top);

        // Swap q1 and q2
        swap(q1, q2);

        return top;
    }

    bool empty() {
        return q1.empty();
    }
};
```

## Test Cases
```
Input: push(1), push(2), push(3), pop(), push(4), top()
Output: 3, 4
```

## Key Takeaways
- We can implement a stack using two queues by moving all elements from one queue to the other except the last one when popping an element.
- The push operation has a time complexity of O(1), while the pop operation has a time complexity of O(n).
- The space complexity is O(n), where n is the number of elements in the stack.