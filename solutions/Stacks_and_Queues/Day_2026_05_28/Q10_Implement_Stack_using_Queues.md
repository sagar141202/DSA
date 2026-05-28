# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes an element from the top of the stack. The problem constraints are that we can only use two queues and no other data structures. For example, if we push the elements 1, 2, and 3, the stack should return 3 when we pop an element, then 2, and finally 1.

## Approach
We will use two queues to implement the stack. The first queue will store the elements of the stack, and the second queue will be used to reverse the order of the elements when we pop an element. We will achieve this by moving all elements except the last one from the first queue to the second queue, then removing the last element from the first queue.

## Complexity
- Time: O(n) for pop operation, O(1) for push operation
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
    stack.push(3);
    cout << stack.top() << endl;  // prints 3
    cout << stack.pop() << endl;   // prints 3
    cout << stack.pop() << endl;   // prints 2
    cout << stack.pop() << endl;   // prints 1
    return 0;
}
```

## Test Cases
```
Input: push(1), push(2), push(3), top(), pop(), pop(), pop()
Output: 3, 3, 2, 1
```

## Key Takeaways
- We can implement a stack using two queues by using one queue to store the elements and the other queue to reverse the order of the elements when we pop an element.
- The time complexity of the pop operation is O(n) because we need to move all elements except the last one from the first queue to the second queue.
- The space complexity is O(n) where n is the number of elements in the stack because we need to store all elements in the two queues.