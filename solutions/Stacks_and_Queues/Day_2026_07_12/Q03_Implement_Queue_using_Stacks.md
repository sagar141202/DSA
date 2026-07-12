# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added will be the first one to be removed. The queue should support the following operations: `push(x)` - Push element x to the back of queue, `pop()` - Removes the element from the front of queue, `peek()` - Get the front element, `empty()` - Return whether the queue is empty. The input will be a sequence of these operations. For example, if we have the operations `push(1)`, `push(2)`, `peek()`, `pop()`, `empty()`, the output should be `1`, `1` (since `1` is at the front after pushing `1` and `2`), and then `false` (since the queue is not empty after popping one element).

## Approach
We can use two stacks to implement the queue. One stack will be used for pushing elements and the other for popping and peeking elements. When an element is pushed, it goes into the first stack. When an element needs to be popped or peeked, we transfer elements from the first stack to the second stack, which reverses the order, allowing us to access the front element of the queue.

## Complexity
- Time: O(1) for push, amortized O(1) for pop and peek
- Space: O(n), where n is the number of elements in the queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MyQueue {
private:
    stack<int> s1; // stack for pushing elements
    stack<int> s2; // stack for popping and peeking elements

public:
    /** Push element x to the back of queue. */
    void push(int x) {
        // Simply push the element into the first stack
        s1.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        // If s2 is empty, transfer elements from s1 to s2
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        // Pop and return the top element from s2
        int top = s2.top();
        s2.pop();
        return top;
    }

    /** Get the front element. */
    int peek() {
        // If s2 is empty, transfer elements from s1 to s2
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        // Return the top element from s2 without removing it
        return s2.top();
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        // The queue is empty if both stacks are empty
        return s1.empty() && s2.empty();
    }
};

int main() {
    MyQueue q;
    q.push(1);
    q.push(2);
    cout << q.peek() << endl; // Output: 1
    cout << q.pop() << endl;  // Output: 1
    cout << q.empty() << endl; // Output: 0 (false)
    return 0;
}
```

## Test Cases
```
Input: push(1), push(2), peek(), pop(), empty()
Output: 1, 1, 0
```

## Key Takeaways
- We use two stacks, `s1` for pushing elements and `s2` for popping and peeking elements.
- The `pop` and `peek` operations have an amortized time complexity of O(1) because although transferring elements from `s1` to `s2` takes O(n) time, this is done only when `s2` is empty, and subsequent `pop` and `peek` operations take O(1) time until `s2` is empty again.