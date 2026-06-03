# Implement Queue using Stacks

## Problem Statement
Implement a queue using two stacks. A queue is a First-In-First-Out (FIFO) data structure, where the first element added will be the first one to be removed. The queue should support the following operations: `push(x)` - Push element x to the back of queue, `pop()` - Removes the element from the front of queue, `peek()` - Get the front element, `empty()` - Return whether the queue is empty. The input will be a series of these operations, and the output should be the result of each operation. For example, given the operations `push(1)`, `push(2)`, `peek()`, `pop()`, `empty()`, the output should be `1`, `1`.

## Approach
We can implement a queue using two stacks by using one stack for enqueue operations and the other stack for dequeue operations. When an element is added to the queue, it is pushed onto the first stack. When an element is removed from the queue, the elements are popped from the first stack and pushed onto the second stack, then the top element is popped from the second stack.

## Complexity
- Time: O(1) for push, O(n) for pop and peek in the worst case (when the second stack is empty)
- Space: O(n) for storing the elements in the two stacks

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MyQueue {
private:
    stack<int> s1, s2;
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
        int res = s2.top();
        s2.pop();
        return res;
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
Input: 
push(1)
push(2)
peek()
pop()
empty()
Output: 
1
1
false
```

## Key Takeaways
- We can implement a queue using two stacks, one for enqueue operations and the other for dequeue operations.
- The time complexity of push operation is O(1), while the time complexity of pop and peek operations is O(n) in the worst case.
- The space complexity is O(n) for storing the elements in the two stacks.