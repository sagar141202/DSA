# Implement Stack using Queues

## Problem Statement
Implement a stack using two queues. The stack should support the standard push and pop operations. The push operation adds an element to the top of the stack, while the pop operation removes the element from the top of the stack. The problem constraints are that we can only use queues to implement the stack, and we cannot use any other data structures. For example, if we push the elements 1, 2, and 3 onto the stack, the top of the stack should be 3, and popping from the stack should return 3, then 2, and finally 1.

## Approach
We will use two queues to implement the stack. One queue will be used to store the elements, and the other queue will be used to rotate the elements to the front of the queue when a push operation is performed. The intuition is to always keep the top element of the stack at the front of the first queue.

## Complexity
- Time: O(n) for push operation and O(1) for pop operation (amortized)
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
    void push(int x) {
        // Add the new element to the empty queue
        q2.push(x);
        
        // Move all elements from q1 to q2
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }
        
        // Swap q1 and q2
        swap(q1, q2);
    }

    void pop() {
        // Check if the stack is empty
        if (q1.empty()) {
            return;
        }
        
        // Remove the front element from q1
        q1.pop();
    }

    int top() {
        // Return the front element of q1
        return q1.front();
    }

    bool empty() {
        // Check if q1 is empty
        return q1.empty();
    }
};

int main() {
    Stack stack;
    stack.push(1);
    stack.push(2);
    stack.push(3);
    cout << stack.top() << endl;  // Output: 3
    stack.pop();
    cout << stack.top() << endl;  // Output: 2
    return 0;
}
```

## Test Cases
```
Input: push(1), push(2), push(3), top(), pop(), top()
Output: 3, 2
```

## Key Takeaways
- We can implement a stack using two queues by rotating the elements to the front of the queue when a push operation is performed.
- The time complexity of the push operation is O(n) because we need to move all elements from one queue to the other, while the time complexity of the pop operation is O(1) because we can simply remove the front element from the queue.
- The space complexity is O(n) because we need to store all elements in the queues.