# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element added to the queue will be the first one to be removed. The queue should support the following operations: `push(x)` - Push element x to the back of queue, `pop()` - Removes the element from the front of queue, `peek()` - Get the front element, `empty()` - Return whether the queue is empty. The input will be a sequence of these operations. For example, given the sequence `push(1)`, `push(2)`, `peek()`, `pop()`, `empty()`, the output should be `1`, `1`. The constraints are that the number of elements in the queue will not exceed 1000 at any point, and the number of operations will not exceed 1000.

## Approach
We will use two stacks to implement the queue. The first stack will be used to push elements, and the second stack will be used to pop elements. When we need to pop an element, we will transfer all elements from the first stack to the second stack, and then pop the top element from the second stack.

## Complexity
- Time: O(1) for push, O(n) for pop, peek, and empty in the worst case
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MyQueue {
private:
    stack<int> s1, s2;
public:
    /** Push element x to the back of queue */
    void push(int x) {
        // Push element x to the first stack
        s1.push(x);
    }

    /** Removes the element from the front of queue */
    int pop() {
        // If the second stack is empty, transfer elements from the first stack
        if (s2.empty()) {
            while (!s1.empty()) {
                // Transfer elements from the first stack to the second stack
                s2.push(s1.top());
                s1.pop();
            }
        }
        // Pop the top element from the second stack
        int top = s2.top();
        s2.pop();
        return top;
    }

    /** Get the front element */
    int peek() {
        // If the second stack is empty, transfer elements from the first stack
        if (s2.empty()) {
            while (!s1.empty()) {
                // Transfer elements from the first stack to the second stack
                s2.push(s1.top());
                s1.pop();
            }
        }
        // Return the top element from the second stack
        return s2.top();
    }

    /** Returns whether the queue is empty */
    bool empty() {
        // Return whether both stacks are empty
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
- We can implement a queue using two stacks by transferring elements from one stack to the other when we need to pop an element.
- The time complexity of push is O(1), but the time complexity of pop, peek, and empty can be O(n) in the worst case.
- The space complexity is O(n), where n is the number of elements in the queue.