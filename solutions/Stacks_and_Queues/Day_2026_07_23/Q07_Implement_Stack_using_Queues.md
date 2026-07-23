# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The implementation should be efficient in terms of time and space complexity. For example, given the sequence of operations: push(1), push(2), pop(), push(3), pop(), the output should be: 2, 3.

## Approach
We can implement a stack using two queues by using one queue as the main storage and the other queue as a temporary buffer. When pushing an element, we add it to the end of the main queue. When popping an element, we move all elements except the last one to the temporary queue, then dequeue the last element from the main queue.

## Complexity
- Time: O(n) for pop operation, O(1) for push operation
- Space: O(n) for storing the elements

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Stack {
private:
    queue<int> q1, q2;
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

int main() {
    Stack stack;
    stack.push(1);
    stack.push(2);
    cout << stack.pop() << endl; // prints 2
    stack.push(3);
    cout << stack.pop() << endl; // prints 3
    return 0;
}
```

## Test Cases
```
Input: push(1), push(2), pop(), push(3), pop()
Output: 2, 3
Input: push(1), pop(), push(2), pop()
Output: 1, 2
```

## Key Takeaways
- We can use two queues to implement a stack with efficient push and pop operations.
- The time complexity of the pop operation is O(n) because we need to move all elements except the last one to the temporary queue.
- The space complexity is O(n) because we need to store all elements in the queues.