# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added will be the first one to be removed. The queue should support the following operations: `push(x)` - Push element x to the back of queue, `pop()` - Removes the element from the front of queue, `peek()` - Get the front element, `empty()` - Return whether the queue is empty. The input will be a sequence of operations, and the output should be the result of each operation. For example, given the sequence of operations `push(1)`, `push(2)`, `peek()`, `pop()`, `empty()`, the output should be `1`, `1`.

## Approach
We can use two stacks to implement a queue. The first stack will be used to store the elements, and the second stack will be used to reverse the order of the elements when we need to pop or peek an element. When we push an element, we simply push it onto the first stack. When we pop or peek an element, we pop all elements from the first stack and push them onto the second stack, then pop or peek the top element from the second stack.

## Complexity
- Time: O(1) for push, O(n) for pop and peek in the worst case
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MyQueue {
private:
    stack<int> s1, s2;
public:
    /** Push element x to the back of queue. */
    void push(int x) {
        s1.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        int temp = s2.top();
        s2.pop();
        return temp;
    }

    /** Get the front element. */
    int peek() {
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        return s2.top();
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        return s1.empty() && s2.empty();
    }
};
```

## Test Cases
```
Input: push(1), push(2), peek(), pop(), empty()
Output: 1, 1, false
```

## Key Takeaways
- We can use two stacks to implement a queue, where one stack is used to store the elements and the other stack is used to reverse the order of the elements when needed.
- The time complexity of push operation is O(1), and the time complexity of pop and peek operations is O(n) in the worst case.
- The space complexity is O(n), where n is the number of elements in the queue.