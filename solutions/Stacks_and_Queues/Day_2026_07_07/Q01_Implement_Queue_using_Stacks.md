# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, meaning the first element that is added will be the first one to be removed. The queue should support the following operations: `push(x)` - Push element x to the back of queue, `pop()` - Removes the element from the front of queue, `peek()` - Get the front element, `empty()` - Return whether the queue is empty. The input will be a sequence of these operations, and the output should be the result of each operation. For example, given the sequence of operations `push(1)`, `push(2)`, `peek()`, `pop()`, `empty()`, the output should be `1`, `false`.

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
    stack<int> s1;
    stack<int> s2;

public:
    // Push element x to the back of queue
    void push(int x) {
        s1.push(x);
    }

    // Removes the element from the front of queue
    int pop() {
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        int top = s2.top();
        s2.pop();
        return top;
    }

    // Get the front element
    int peek() {
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        return s2.top();
    }

    // Return whether the queue is empty
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
- We can use two stacks to implement a queue by reversing the order of the elements when we need to pop or peek an element.
- The push operation has a time complexity of O(1), while the pop and peek operations have a time complexity of O(n) in the worst case.
- The space complexity is O(n), where n is the number of elements in the queue.