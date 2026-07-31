# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The problem constraints are that we can only use two queues to implement the stack, and we should minimize the time and space complexity of the operations. For example, given the operations `push(1)`, `push(2)`, `pop()`, `push(3)`, `pop()`, the output should be `2`, `3`.

## Approach
We can use two queues to implement a stack by maintaining one queue as the main stack and the other as a temporary queue. When pushing an element, we add it to the temporary queue and then move all elements from the main queue to the temporary queue. When popping an element, we simply remove it from the main queue.

## Complexity
- Time: O(n) for push operation and O(1) for pop operation
- Space: O(n) where n is the number of elements in the stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
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
- We can implement a stack using two queues by maintaining one queue as the main stack and the other as a temporary queue.
- The push operation has a time complexity of O(n) due to the movement of elements from the main queue to the temporary queue.
- The pop operation has a time complexity of O(1) since we simply remove the front element from the main queue.