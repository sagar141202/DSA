# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The stack is empty if both queues are empty. For example, if we push elements 1, 2, and 3, the top of the stack should be 3, and after popping, the top of the stack should be 2.

## Approach
We will use two queues, q1 and q2, to implement the stack. The push operation will add elements to the end of q1, and the pop operation will remove elements from the front of q1 after moving all elements except the last one to q2.

## Complexity
- Time: O(n) for pop operation, O(1) for push operation
- Space: O(n) for storing n elements

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Stack {
private:
    queue<int> q1, q2;
public:
    // Push element x onto stack
    void push(int x) {
        q1.push(x);
    }

    // Removes the element on top of the stack
    void pop() {
        if (q1.empty()) {
            return;
        }
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        q1.pop();
        queue<int> temp = q1;
        q1 = q2;
        q2 = temp;
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
        int topElement = q1.front();
        q2.push(q1.front());
        q1.pop();
        queue<int> temp = q1;
        q1 = q2;
        q2 = temp;
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
Input: push(1), push(2), push(3), top(), pop(), top()
Output: 3, 2
```

## Key Takeaways
- We can implement a stack using two queues by moving all elements except the last one to the second queue for the pop operation.
- The time complexity for the pop operation is O(n) because we need to move all elements except the last one to the second queue.
- The space complexity is O(n) because we need to store n elements in the queues.